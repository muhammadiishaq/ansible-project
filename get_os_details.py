#!/usr/bin/env python3

import os
import csv
import json
from datetime import *

date = date.today()
time1 = datetime.now()

#filepath = time1.strftime("Daily_reports_%Y-%m-%d_%H:%M:%S.csv")

filepath = "Daily_report.csv"
json_file = "my_linux_cmd.json"

with open(json_file) as file:
    my_dict=json.load(file)
os_name = os.popen(my_dict['os_flavour']).read().strip('\n')
print(os_name)
if os_name == "ubuntu" or os_name == "centos":
    print("This is a Ubuntu or CentOS system are found we are collecting information , so please wait..!!!.")

    #hostname details
    hostname = os.popen(my_dict['hostname']).read()
    print(f"Hostname: {hostname}")

    #ip address details
    ip=os.popen(my_dict['ip_address']).read()
    print(f"IP Address: {ip}")

    #file storage details
    df_details = os.popen(my_dict['df_details']).read()
    print("File Storage Details:")
    print(df_details)

    #storing varaible into list for inserting CSV data
    header_csv = my_dict['header_para']
    header_csv = [str (x) for x in header_csv]
    print(f"Header CSV: {header_csv}")


    #data for CSV file
    data_csv = [hostname, ip, df_details]

    file1 = open(filepath, "a+")
    writer = csv.writer(file1)
    writer.writerow(header_csv)
    writer.writerow(data_csv)
    file1.close()

    #done 
    print("Data has been written to Daily_report.csv successfully.")
else:
    print("This is not a Ubuntu or CentOS system, so we are not collecting information.")
    print("Please run this script on Ubuntu or CentOS system to collect the required information.")