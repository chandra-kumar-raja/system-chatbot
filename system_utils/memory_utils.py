import psutil
from functools import lru_cache

@lru_cache(maxsize=1)
def get_memory_info():
    """Return detailed memory (RAM) information."""
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    memory_info = {
        "Total Memory (GB)": round(memory.total / (1024 ** 3), 2),
        "Used Memory (GB)": round(memory.used / (1024 ** 3), 2),
        "Free Memory (GB)": round(memory.available / (1024 ** 3), 2),
        "Memory Usage (%)": memory.percent,
        "Swap Total (GB)": round(swap.total / (1024 ** 3), 2),
        "Swap Used (GB)": round(swap.used / (1024 ** 3), 2),
        "Swap Usage (%)": swap.percent
    }
    return memory_info
