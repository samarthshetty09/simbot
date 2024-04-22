import psutil
import GPUtil
import time
import csv

def find_coppeliasim_process():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'coppeliaSim' == proc.info['name']:
            return proc
    return None

def monitor_resources(process):
    data = []  # List to hold all the resource usage data
    count = 0
    try:
        while count < 60:
            # CPU and Memory Usage
            cpu_usage = process.cpu_percent(interval=1)
            memory_usage = process.memory_percent()
            
            # GPU Usage
            gpus = GPUtil.getGPUs()
            gpu_usage = [gpu.load * 100 for gpu in gpus]  # List of GPU usages in percentage
            
            # Collect data in the list
            data.append([count, cpu_usage, memory_usage, gpu_usage])
            time.sleep(1)  # Sleep for 1 second to pace the output
            count += 1
    except (psutil.NoSuchProcess, psutil.AccessDenied, KeyboardInterrupt):
        print("Monitoring stopped. Process has been terminated, access denied, or interrupted.")
    return data

def write_to_csv(data):
    with open('resource_usage.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Iteration', 'CPU Usage (%)', 'Memory Usage (%)', 'GPU Usage (%)'])
        for row in data:
            writer.writerow(row)

def main():
    coppeliasim_process = find_coppeliasim_process()
    if coppeliasim_process:
        print(f"Found CoppeliaSim process with PID: {coppeliasim_process.pid}")
        data = monitor_resources(coppeliasim_process)
        write_to_csv(data)
    else:
        print("CoppeliaSim process not found. Make sure CoppeliaSim is running.")

if __name__ == '__main__':
    main()
