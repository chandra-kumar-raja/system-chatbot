import psutil
import platform
import time
from system_utils.cpu_utils import get_cpu_info
from system_utils.memory_utils import get_memory_info
from system_utils.battery_utils import get_battery_info
from system_utils.network_utils import get_network_info



def get_system_specs():

    specs = {
        "OS": platform.system() + " " + platform.release(),
        "CPU Info": get_cpu_info(),
        "Memory Info": get_memory_info(),
        "Battery Info": get_battery_info(),
        "Network Info": get_network_info()

    }
    return specs
