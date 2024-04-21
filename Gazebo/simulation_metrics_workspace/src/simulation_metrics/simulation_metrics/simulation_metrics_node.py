import psutil
import subprocess
import time
import csv

def get_cpu_metrics():
    cpu_percent = psutil.cpu_percent()
    cpu_usage = psutil.cpu_percent(percpu=True)
    return cpu_percent, cpu_usage

def get_memory_metrics():
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    memory_usage = memory_info.used / (1024 ** 2)  # Convert to MB
    return memory_percent, memory_usage

def get_gpu_utilization():
    gpu_utilization = subprocess.check_output("nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits", shell=True).decode("utf-8").strip()
    return float(gpu_utilization)

def calculate_fps(frame_count, start_time):
    elapsed_time = time.time() - start_time
    if elapsed_time >= 1:
        fps = frame_count / elapsed_time
        return fps
    else:
        return None

def main():
    simulation_duration = 60  # Duration in seconds
    start_time = time.time()
    frame_count = 0

    # Initialize CSV file
    with open('simulation_metrics.csv', mode='w', newline='') as metrics_file:
        metrics_writer = csv.writer(metrics_file)
        metrics_writer.writerow(['Time', 'CPU Usage (%)', 'CPU Usage (per core)', 'Memory Usage (%)', 'Memory Usage (MB)', 'GPU Utilization (%)', 'FPS', 'Real-Time Factor'])

        while time.time() - start_time < simulation_duration:
            # Get metrics
            cpu_percent, cpu_usage = get_cpu_metrics()
            memory_percent, memory_usage = get_memory_metrics()
            gpu_utilization = get_gpu_utilization()
            fps = calculate_fps(frame_count, start_time)

            # Calculate real-time factor
            current_time = time.time()
            elapsed_simulation_time = current_time - start_time
            real_time_factor = elapsed_simulation_time / (frame_count + 1)  # Add 1 to avoid division by zero
            real_time_factor = min(1.0, real_time_factor)  # Ensure real-time factor is at most 1

            # Write metrics to CSV
            metrics_writer.writerow([elapsed_simulation_time, cpu_percent, cpu_usage, memory_percent, memory_usage, gpu_utilization, fps, real_time_factor])

            # Print metrics to console
            print(f"Time: {elapsed_simulation_time:.2f}s, CPU Usage: {cpu_percent:.2f}%, CPU Usage (per core): {cpu_usage}, Memory Usage: {memory_percent:.2f}%, Memory Usage: {memory_usage:.2f} MB, GPU Utilization: {gpu_utilization:.2f}%, FPS: {fps:.2f}, Real-Time Factor: {real_time_factor:.2f}")

            # Increment frame count for FPS calculation
            frame_count += 1

            # Sleep for 1 second
            time.sleep(1)

if __name__ == "__main__":
    main()

