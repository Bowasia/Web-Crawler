#!/usr/bin/env bash
firefox https://www.facebook.com/narisa.thjakan/about


xdotool mousemove 1260 365 sleep 5
xdotool click 3 key P sleep 2
xdotool type 'to_parse2'
xdotool key KP_Delete key KP_Delete key KP_Delete key KP_Delete key KP_Delete
xdotool type '.txt'
xdotool key KP_Enter sleep 1 key KP_Enter sleep 2
xdotool key alt+Tab sleep 2
cd Downloads
xdg-open to_parse2.txt


#xdg-open
