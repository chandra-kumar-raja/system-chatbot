import psutil
import subprocess
import platform
from functools import lru_cache

@lru_cache(maxsize=1)
def get_battery_info():
    """
    Returns detailed battery info for macOS and other OSes.
    """
    system = platform.system()
    battery_data = {}

    if system == "Darwin":
        try:
            output = subprocess.check_output(
                ["pmset", "-g", "batt"], text=True
            ).strip()

            for line in output.split("\n"):
                if "%" in line:
                    parts = line.split(";")
                    percent = parts[0].split()[-1]
                    status = parts[1].strip() if len(parts) > 1 else "Unknown"
                    remaining = parts[2].strip() if len(parts) > 2 else "Unknown"

                    battery_data = {
                        "Battery Percentage": percent,
                        "Status": status,
                        "Remaining": remaining
                    }
                    break

        except Exception as e:
            battery_data = {"Error": f"Unable to fetch battery info: {e}"}

    else:
        try:
            battery = psutil.sensors_battery()
            if battery:
                battery_data = {
                    "Battery Percentage": f"{battery.percent}%",
                    "Power Plugged": battery.power_plugged,
                    "Time Left (sec)": battery.secsleft
                }
            else:
                battery_data = {"Battery Percentage": "N/A"}
        except Exception as e:
            battery_data = {"Error": str(e)}

    return battery_data
