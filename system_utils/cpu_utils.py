import psutil
from functools import lru_cache

@lru_cache(maxsize=1)
def get_cpu_info():
    """Return detailed CPU information."""
    cpu_info = {
        "CPU Cores (Logical)": psutil.cpu_count(logical=True),
        "CPU Cores (Physical)": psutil.cpu_count(logical=False),
        "CPU Usage (%)": psutil.cpu_percent(interval=0.1),
        "CPU Frequency (MHz)": psutil.cpu_freq().current if psutil.cpu_freq() else "N/A",
        "CPU Load (1, 5, 15 min avg)": psutil.getloadavg() if hasattr(psutil, "getloadavg") else "N/A"
    }
    return cpu_info
