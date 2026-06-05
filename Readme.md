# Waybar Config — Clean Waybar setup

A clean, modern, and minimal Waybar configuration with custom helper modules.

![Waybar Preview](images/image.png)

## Preview with wallpaper

![Waybar Preview](images/desktop.png)

## Main Highlights

- **Todo Module**: A custom Rofi-based task tracker integrated into Waybar.
- **Daemons Monitor**: A python-based systemd running services monitor displaying active system and user services.
- **Battery Monitor Daemon**: A background python daemon displaying notifications and custom-themed Rofi alerts on charging and low battery events.

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

- `launch.sh` — Startup script to launch Waybar, Swaync, and the battery monitor daemon.
- `scripts/daemons.py` — Python script used by `custom/daemons` to gather systemd services status.
- `scripts/todo/todo.sh` — Script for the main `custom/todo` text updates and click events.
- `scripts/todo/todo_popup.sh` — Rofi-popup task manager script.
- `scripts/battery_monitor.py` — Python background daemon that monitors battery level and status.
- `scripts/battery_custom.py` — Python script for custom battery indicator and power-saver status.
- `scripts/toggle_power_saver.sh` — Shell script to toggle system power saving mode.
- `scripts/battery_rofi.rasi` — Transparent Rofi theme for battery alert overlays.

---

## Power saving mode & Notifications Detail

![Waybar Preview](images/powersaving.png)
![Waybar Preview](images/normal.png)

The battery status is displayed using a unified custom module (`custom/battery`):
- **Dynamic Leaf Icon**: When the laptop is placed in `power-saver` mode, the standard battery status icon is automatically replaced by a green leaf icon (``).
- **Toggle Power Saver**: Clicking the battery percentage (or leaf icon) in Waybar executes `scripts/toggle_power_saver.sh`, which toggles between `balanced` and `power-saver` profiles. The changes reflect instantly on the bar via custom signaling (`SIGRTMIN+8`). It also triggers a 2-second Rofi screen alert and a desktop notification.

### What does Power Saving Mode (`power-saver`) do?
Under `power-profiles-daemon`, the `power-saver` profile optimizes system battery life by adjusting the following kernel and hardware parameters:
1. **CPU Energy Performance Preference (EPP)**: Biases CPU drivers (like `amd_pstate` or `intel_pstate`) toward energy savings (sets EPP to `power` or `power_saver`), which caps peak CPU clock speeds and reduces voltage scaling.
2. **Platform Thermal Profile**: Signals ACPI/UEFI firmware to restrict thermal design power (TDP) limits, resulting in a cooler, quieter laptop with less active cooling power consumption.
3. **Aggressive Low Power States**: Speeds up device transition into idle/deep sleep modes for connected PCI/SATA link interfaces.

---

## Battery Monitor & Notifications Detail

![Waybar Preview](images/charging.png)

Additionally, the background daemon `scripts/battery_monitor.py` is executed by `launch.sh` on startup and checks the battery status every 5 seconds. It triggers alerts under the following conditions:

- **Charger Connected**: Sends a desktop notification and opens a transparent Rofi overlay: `  Charging: X%` (auto-closes after 3 seconds).
- **Low Battery (≤30%)**: Sends a critical desktop notification and opens a Rofi warning overlay: `  Battery Low: X%` (auto-closes after 5 seconds).
- **Critical Battery (≤15%)**: Sends a critical desktop notification and opens a Rofi warning overlay: `  Battery Critical: X%` (auto-closes after 5 seconds).

