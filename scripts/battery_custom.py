#!/usr/bin/env python3
import json
import os
import subprocess

def get_battery_info():
    bat_dir = None
    if os.path.exists('/sys/class/power_supply'):
        for d in os.listdir('/sys/class/power_supply'):
            if d.startswith('BAT'):
                bat_dir = os.path.join('/sys/class/power_supply', d)
                break
    if not bat_dir:
        return 50, "Unknown"
    
    try:
        with open(os.path.join(bat_dir, 'capacity'), 'r') as f:
            capacity = int(f.read().strip())
    except Exception:
        capacity = 50
        
    try:
        with open(os.path.join(bat_dir, 'status'), 'r') as f:
            status = f.read().strip()
    except Exception:
        status = "Unknown"
        
    return capacity, status

def get_power_profile():
    try:
        res = subprocess.run(['powerprofilesctl', 'get'], capture_output=True, text=True)
        return res.stdout.strip()
    except Exception:
        return "balanced"

def main():
    capacity, status = get_battery_info()
    profile = get_power_profile()
    
    if profile == "power-saver":
        icon = ""
        css_class = "power-saver"
    else:
        css_class = "normal"
        if status == "Charging" or status == "Full":
            icon = ""
            css_class = "charging"
        else:
            icons = ["", "", "", "", ""]
            idx = min(capacity // 20, 4)
            icon = icons[idx]
            
    if capacity <= 15:
        css_class += " critical"
    elif capacity <= 30:
        css_class += " warning"
        
    text = f"{icon}  {capacity}%"
    tooltip = f"Battery: {capacity}%\nStatus: {status}\nProfile: {profile.capitalize()}"
    
    out = {
        "text": text,
        "tooltip": tooltip,
        "class": css_class
    }
    print(json.dumps(out))

if __name__ == "__main__":
    main()
