
from system_utils.cpu_utils import get_cpu_info
from system_utils.memory_utils import get_memory_info
from system_utils.battery_utils import get_battery_info
from system_utils.network_utils import get_network_info



def get_system_specs(user_input: str, last_topic: str = None):
    """fetch only the relevant system specs based on user input keywords (battery, cpu, memory, network)."""
    user_input_lower = user_input.lower()
    specs = {}
    current_topic = None

    if any(k in user_input_lower for k in ["battery", "charge", "power"]):
        specs.update(get_battery_info())
        current_topic = "battery"

    elif any(k in user_input_lower for k in ["cpu", "processor", "core"]):
        specs.update(get_cpu_info())
        current_topic = "cpu"

    elif any(k in user_input_lower for k in ["memory", "ram", "usage"]):
        specs.update(get_memory_info())
        current_topic = "memory"

    elif any(k in user_input_lower for k in ["network", "internet", "wifi", "speed"]):
        specs.update(get_network_info())
        current_topic = "network"

    else:
        if last_topic == "battery":
            specs.update(get_battery_info())
        elif last_topic == "cpu":
            specs.update(get_cpu_info())
        elif last_topic == "memory":
            specs.update(get_memory_info())
        elif last_topic == "network":
            specs.update(get_network_info())
        current_topic = last_topic

    return specs, current_topic