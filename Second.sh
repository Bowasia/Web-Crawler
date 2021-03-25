#!/usr/bin/env bash

#edit url
start_url="https://www.facebook.com/hashtag/%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%AB%E0%B8%B4%E0%B9%89%E0%B8%A7%E0%B8%97%E0%B8%B8%E0%B8%81%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87"

#edit scroll times
scroll=1000

chromium $start_url
sleep 3

for ((i=1;i<=$scroll;i++))
do
  xdotool key space
  sleep 0.1
done

xdotool key alt+f sleep 0.5 key a sleep 1
file_name='FB_rubhewtookyang_'$(date +%d_%m_%Y_%X)
xdotool type $file_name
xdotool key KP_Enter sleep 4 key ctrl+w
mv ~/Downloads/$file_name.html ~/Documents/Web-Crawler/save_page
sleep 3
rm -r ~/Downloads/$file_name'_files'
cd ~/Documents/Web-Crawler/save_page

python3 ../soup_parse.py "${file_name}"
#python3 ../parse_query.py $file_name.html
