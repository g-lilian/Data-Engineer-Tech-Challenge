# Section 1: Data Pipelines

Install dependencies:
- pyspark v3.3.1
- pandas v1.5.1

Install Hadoop by following the instructions [here](https://medium.com/@farhan0syakir/setup-pycharm-hadoop-pyspark-development-on-windows-without-installing-hadoop-6aa7bde7d189).

Execute the data pipeline manually:
```
python3 process_applications.py
```

As I'm using Windows OS, Windows Task Scheduler is the most convenient tool for scheduling. For Linux/Mac OS, crontab can be used. For more complex workflows, Airflow is recommended.

To schedule the task on Windows, follow instructions in this [tutorial](https://www.jcchouinard.com/python-automation-using-task-scheduler).

Example configuration:
![image](images/config_1.png)
![image](images/config_2.png)
