from datetime import datetime
from glob import glob
import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import *


# Load CSVs in folder with latest date time into Spark DF
# Assumptions: folders are named in %Y%m%d%H format and we always want to process the latest data
def read_csvs(spark):
    DT_FORMAT = "%Y%m%d%H"

    latest_dt = datetime.strptime("2022112200", DT_FORMAT)
    latest_dt_path = ""
    for folder in glob("applications/*", recursive=False):
        dt = datetime.strptime(folder.split("\\")[-1], DT_FORMAT)
        if dt >= latest_dt:
            latest_dt = dt
            latest_dt_path = folder

    df = None
    for file in glob(latest_dt_path + "/*"):
        if not df:
            df = spark.read.csv(file, header=True, inferSchema=True)
        else:
            df.union(spark.read.csv(file, header=True, inferSchema=True))

    return datetime.strftime(latest_dt, DT_FORMAT), df


# Caveat: for some dates, it's impossible to distinguish between month and day
def to_date_(col, formats=("yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy", "yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy")):
    return coalesce(*[to_date(col, f) for f in formats])


def process_applications():
    USER = os.getenv('username')
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    os.environ['HADOOP_HOME'] = f"C:/Users/{USER}/hadoop/hadoop-3.3.4"

    # Run locally with 1 core
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("Application Processor") \
        .getOrCreate()

    dt, df = read_csvs(spark)

    # Transform DF into required format
    df = df.withColumn("first_name", split(col("name"), ' ').getItem(0)) \
        .withColumn("last_name", split(col("name"), ' ').getItem(1)) \
        .withColumn("mobile_no", regexp_extract(col("mobile_no"), "\\d+", 0)) \
        .withColumn("above_18", when(
            months_between(to_date(lit("2022-01-01"), format='yyyy-MM-dd'), to_date_(col("date_of_birth"))) > 18 * 12,
            lit(True)) \
            .otherwise(lit(False))) \
        .withColumn("date_of_birth", date_format(to_date_(col("date_of_birth")), "yyyyMMdd")) \
        .withColumn("membership_id",
            concat(col("last_name"), lit("_"), substring(sha2(col("date_of_birth"), 256), 1, 5))) \
        .select(col("first_name"), col("last_name"), col("membership_id"), col("date_of_birth"), col("email"),
            col("mobile_no"), col("above_18"))

    # Filter successful and failed applications
    valid_email_regex = "^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\\.(?:com|net)$"
    # Applications with invalid dates, like 31 Feb, are not successful
    success_df = df.filter(col("date_of_birth").isNotNull()) \
        .filter(length(col("mobile_no")) == 8) \
        .filter(col("above_18") == True) \
        .filter(col("email").rlike(valid_email_regex)) \
        .filter(col("name").isNotNull())
    failure_df = df.subtract(success_df)

    # Write output to different CSV files
    # Use pandas here for simplicity of writing to one CSV file
    success_df.toPandas().to_csv(f"success/{dt}.csv", header=True)
    failure_df.toPandas().to_csv(f"failure/{dt}.csv", header=True)

    spark.stop()


if __name__ == "__main__":
    process_applications()
