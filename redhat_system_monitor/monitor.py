import psutil
import time
import os

def clear_screen():
    os.system("clear")

def get_system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return cpu, memory, disk

def display_info():
    cpu, memory, disk = get_system_info()

    print("===== Red Hat System Monitor =====\n")
    print(f"CPU Usage: {cpu}%\n")

    print("Memory Usage:")
    print(f"  Total: {round(memory.total / (1024**3), 2)} GB")
    print(f"  Used: {round(memory.used / (1024**3), 2)} GB")
    print(f"  Percentage: {memory.percent}%\n")

    print("Disk Usage (/):")
    print(f"  Total: {round(disk.total / (1024**3), 2)} GB")
    print(f"  Used: {round(disk.used / (1024**3), 2)} GB")
    print(f"  Percentage: {disk.percent}%\n")

if __name__ == "__main__":
    while True:
        clear_screen()
        display_info()
        time.sleep(3)
