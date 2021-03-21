#!/usr/bin/env dash
from urllib.parse import urlparse
import csv
import os
import subprocess

with open('data_personal_link_1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
             print(row['Number'], row['Name'], row['Link'])
             obj = urlparse(row['Link'])
             open_this_link = obj[1] + obj[2] + '/about_contact_and_basic_info'
             print(open_this_link)
             print(obj)
             print('\n')
print("start")
subprocess.call("../get_profile.sh",shell=True)
print("End")
