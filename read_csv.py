#!/usr/bin/env bash
from urllib.parse import urlparse
import csv
import os
import subprocess

with open('data_personal_link_1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
             print(row['Number'], row['Name'], row['Link'])
             obj = urlparse(row['Link'])
             path = obj[2]
             query = obj[4]
             id = ''
             for character in query:
                 if character != '&':
                     id = id + character
                 else:
                     break

             path_reverse = str(path[::-1])
             print(path_reverse[0:3])
             if path_reverse[0:3] == "php":
                 open_this_link = obj[1] + path + "?" + id + "&sk=about_contact_and_basic_info"
             else:
                open_this_link = obj[1] + obj[2] + '/about_contact_and_basic_info'
             print(open_this_link)
             print(obj)
             print('\n')
             os.system("firefox " + open_this_link)
             os.system("sleep 2")
             os.system("xdotool key alt+f sleep 0.5 key a sleep 1")
             os.system("xdotool type " + row['Number'] + "_personal")
             os.system("xdotool key KP_Enter sleep 2")
             os.system("mv ~/Downloads/"+ row['Number']+'_personal.html ~/Documents/Web-Crawler/save_page/personal_page')
             os.system("xdotool key ctrl+w")
