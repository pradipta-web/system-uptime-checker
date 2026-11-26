import time
import os
import csv
from datetime import datetime


def get_system_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    return int(uptime_seconds)


def format_uptime(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"

def get_system_info():
    print("\nSYSTEM INFORMATION")
    print("-" * 50)

    print(f"Operating System : {os.name}")
    print(f"Platform         : {psutil.LINUX if os.name == 'posix' else 'Windows'}")
    print(f"CPU Cores        : {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage        : {psutil.cpu_percent(interval=1)}%")


def save_uptime_log(uptime):
    file_exists = os.path.isfile("uptime_history.csv")

    with open("uptime_history.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "System Uptime (Seconds)"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            uptime
        ])


def monitor_uptime():
    print("=" * 50)
    print("          PYTHON SYSTEM UPTIME CHECKER")
    print("=" * 50)

    boot_time = datetime.fromtimestamp(psutil.boot_time())

    print(f"\nSystem Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nMonitoring system uptime...")
    print("Press CTRL+C to stop.\n")

    try:
        while True:
            uptime = get_system_uptime()
            save_uptime_log(uptime)

            print("\033[H\033[J", end="")

            print("=" * 50)
            print("          PYTHON SYSTEM UPTIME CHECKER")
            print("=" * 50)

            print(f"\nSystem Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\nSystem Uptime: {format_uptime(uptime)}")

            print("\nMonitoring system uptime...")
            print("Press CTRL+C to stop.")
            get_system_info()

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")


if __name__ == "__main__":
    import psutil
    monitor_uptime()