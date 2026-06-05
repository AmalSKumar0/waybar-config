#!/bin/bash

killall -9 waybar
killall -9 swaync
pkill -f battery_monitor.py

waybar &
swaync &
/home/amalskumar/.config/waybar/scripts/battery_monitor.py &
