import pandas as pd
import os
import argparse

# create argument parser object
parser = argparse.ArgumentParser(
        description="Input log file path to monitor error messages"
    )

# define an argument for cmd input
parser.add_argument("directory", required=True,  type=str, help="Enter path to log file")

args = parser.parse_args()

# file path for log files
directory = args.directory
log_text = ''
count_error = 0
error_description = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".log"):
            # read the file using reader object and store the text in string object
            file_path = os.path.join(root,file)
            f = open(file_path, 'r')
            log_text = f.readlines()
            f.close()

for i in log_text:
    if 'ERROR' in i:
        count_error += 1
        error_description.append(i)
print(f'Total errors: {count_error}')
print('Error Descriptions: ')
for error in error_description:
    print(error,'\n')
