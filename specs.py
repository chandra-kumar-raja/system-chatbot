import psutil
import platform
import time
from system_utils.cpu_utils import get_cpu_info
from system_utils.memory_utils import get_memory_info
from system_utils.battery_utils import get_battery_info
from system_utils.network_utils import get_network_info



def get_system_specs(user_input, last_topic=None):
    user_input = user_input.lower()

    if any(word in user_input for word in ["battery", "power", "charge"]):
        topic = "battery"
        specs = get_battery_info()
    elif any(word in user_input for word in ["cpu", "processor", "core"]):
        topic = "cpu"
        specs = get_cpu_info()
    elif any(word in user_input for word in ["memory", "ram"]):
        topic = "memory"
        specs = get_memory_info()
    elif any(word in user_input for word in ["network", "internet", "speed", "wifi"]):
        topic = "network"
        specs = get_network_info()
    elif last_topic:
        topic = last_topic
        if topic == "battery":
            specs = get_battery_info()
        elif topic == "cpu":
            specs = get_cpu_info()
        elif topic == "memory":
            specs = get_memory_info()
        elif topic == "network":
            specs = get_network_info()
        else:
            specs = get_system_specs()
    else:
        topic = None
        specs = get_system_specs()

    return specs, topic