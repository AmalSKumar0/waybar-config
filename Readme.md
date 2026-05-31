# Waybar Config — Clean Waybar setup

A clean, modern, and minimal Waybar configuration with custom helper modules.

![Waybar Preview](images/image.png)

## Preview with wallpaper

![Waybar Preview](images/desktop.png)

## Main Highlights

- **Todo Module**: A custom Rofi-based task tracker integrated into Waybar.
- **Daemons Monitor**: A python-based systemd running services monitor displaying active system and user services.

---

## Included Modules

- **Clock**: Shows current time and calendar tooltip.
- **MPRIS**: Media player controls and title displays (Spotify, etc.).
- **Network**: Displays Wi-Fi or Ethernet download speed and signal strength.
- **Battery**: Battery status with charging indicator.
- **Hyprland Workspaces**: Shows active workspaces.
- **CPU & Memory**: Displays CPU load and RAM/Swap usage details.
- **Temperature**: Monitor system temperatures.
- **Tray**: System tray for background applications.
- **Custom/Todo**: Tracks tasks, shows progress, and launches a task management menu on click.
- **Custom/Daemons**: Displays running systemd services and their uptime on hover.

---

## Configuration & Customization

The layout is defined in `config.jsonc`, and styles are defined in `style.css`. 

### Running Waybar
Run the startup script:
```bash
./launch.sh
```

This will kill any running Waybar or Swaync instance and launch them in the background.

---

## Included Scripts Overview

- `launch.sh` — Startup script to launch Waybar and Swaync.
- `scripts/daemons.py` — Python script used by `custom/daemons` to gather systemd services status.
- `scripts/todo/todo.sh` — Script for the main `custom/todo` text updates and click events.
- `scripts/todo/todo_popup.sh` — Rofi-popup task manager script.
