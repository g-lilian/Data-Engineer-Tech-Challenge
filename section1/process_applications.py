import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import *


# Caveat: for some dates, it's impossible to distinguish between month and day
def to_date_(col, formats=("yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy", "yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy")):
    return coalesce(*[to_date(col, f) for f in formats])


def main():
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    os.environ['HADOOP_HOME'] = "C:/Users/softs/hadoop/hadoop-3.3.4"

    # Run locally with 1 core
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("Application Processor") \
        .getOrCreate()
    sc = spark.sparkContext

    df = spark.read.csv("applications/applications_dataset_1.csv", header=True, inferSchema=True)
    df.printSchema()

    df = df.withColumn("first_name", split(col("name"), ' ').getItem(0)) \
        .withColumn("last_name", split(col("name"), ' ').getItem(1)) \
        .withColumn("above_18", when(
            months_between(to_date(lit("2022-01-01"), format='yyyy-MM-dd'), to_date_(col("date_of_birth"))) > 18 * 12,
            lit(True)) \
            .otherwise(lit(False))) \
        .withColumn("date_of_birth", date_format(to_date_(col("date_of_birth")), "yyyyMMdd")) \
        .withColumn("membership_id",
            concat(col("last_name"), lit("_"), substring(sha2(col("date_of_birth"), 256), 1, 5))) \
        .select(col("first_name"), col("last_name"), col("membership_id"), col("date_of_birth"), col("email"),
            col("mobile_no"), col("above_18"))

    valid_email_regex = "^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\\.(?:com|net)$"
    # Applications with invalid dates, like 31 Feb, are not successful
    success_df = df.filter(col("date_of_birth").isNotNull()) \
        .filter(length(col("mobile_no")) == 8) \
        .filter(col("above_18") == True) \
        .filter(col("email").rlike(valid_email_regex)) \
        .filter(col("name").isNotNull())
    failure_df = df.subtract(success_df)

    success_df.toPandas().to_csv("success/1.csv", header=True)
    failure_df.toPandas().to_csv("failure/1.csv", header=True)


if __name__ == "__main__":
    main()
