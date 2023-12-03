# Airflow Job Monitoring script

The goal of this project was to build a job monitoring script for Airfllow jobs

### Overview
- The python script takes in cmd line argument of log file path of the Airflow job to be analyzed
- The logic loops through all directories and files in the root
- The output is the count of errors and the description of error messages in the task passed in as argument

The below screenshot shows the arguments passed on the cmd line and the ouput displayed on the console

![Screenshot 2023-12-02 at 10 59 15 PM](https://github.com/meetapandit/airflow_log_monitoring/assets/15186489/d8518b3d-9fdd-4510-b770-610f10ea5c3f)

- The red box shows the cmd line argument passed to log_analyzer.py python script
- The argument is passed to "--directory" variable
- The green box shows the output displayed to the console:
  - count_error = 2
  - Error descriptions which shows the detailed text of the errors found in the Airflow task
