import csv
import time
import subprocess
import psutil

# Example function to get CPU usage
def get_cpu_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    return cpu_percent, cpu_usage

# Example function to get memory usage
def get_memory_metrics():
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    memory_usage = memory_info.used / (1024 ** 2)  # Convert to MB
    return memory_percent, memory_usage

# Example function to get CUDA metrics
def get_cuda_metrics():
    # Use NVIDIA Management Library (NVML) to get GPU metrics
    # You may need to install pynvml library: pip install nvidia-ml-py3
    import pynvml
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # Assuming one GPU
    utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
    gpu_percent = utilization.gpu
    gpu_memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    gpu_memory_percent = (gpu_memory_info.used / gpu_memory_info.total) * 100
    gpu_memory_usage = gpu_memory_info.used / (1024 ** 2)  # Convert to MB
    pynvml.nvmlShutdown()
    return gpu_percent, gpu_memory_percent, gpu_memory_usage

# Define simulation duration (in seconds)
simulation_duration = 180  # You can adjust this as needed

# Initialize lists to store metrics
cpu_percentages = []
cpu_usages = []
memory_percentages = []
memory_usages = []
gpu_percentages = []
gpu_memory_percentages = []
gpu_memory_usages = []
fps_list = []
real_time_factors = []

# Main simulation loop
start_time = time.time()
simulation_start_time = time.time()
metrics_start_time = time.time()
frame_count = 0
while time.time() - metrics_start_time < simulation_duration:
    # Record simulation start time
    step_start_time = time.time()
    
    # Get CPU metrics
    cpu_percent, cpu_usage = get_cpu_metrics()
    cpu_percentages.append(cpu_percent)
    cpu_usages.append(cpu_usage)
    
    # Get memory metrics
    memory_percent, memory_usage = get_memory_metrics()
    memory_percentages.append(memory_percent)
    memory_usages.append(memory_usage)
    
    # Get CUDA metrics
    gpu_percent, gpu_memory_percent, gpu_memory_usage = get_cuda_metrics()
    gpu_percentages.append(gpu_percent)
    gpu_memory_percentages.append(gpu_memory_percent)
    gpu_memory_usages.append(gpu_memory_usage)
    
    # Calculate FPS
    frame_count += 1
    if time.time() - start_time >= 1:
        fps = frame_count / (time.time() - start_time)
        fps_list.append(fps)
        frame_count = 0
        start_time = time.time()
    else:
        fps_list.append(None)
    
    # Calculate real-time factor
    elapsed_simulation_time = time.time() - simulation_start_time
    elapsed_real_time = time.time() - start_time
    if elapsed_real_time != 0:
        real_time_factor = elapsed_simulation_time / elapsed_real_time
    else:
        real_time_factor = None
    real_time_factors.append(real_time_factor)
    
    # Print metrics to console
    print(f"Time: {len(cpu_percentages)}s, CPU Usage: {cpu_percent:.2f}%, CPU Usage Per Core: {cpu_usage}, Memory Usage: {memory_percent:.2f}%, Memory Usage: {memory_usage:.2f} MB, GPU Utilization: {gpu_percent:.2f}%, GPU Memory Usage: {gpu_memory_percent:.2f}%, GPU Memory Usage: {gpu_memory_usage:.2f} MB, FPS: {fps_list[-1]}, Real-Time Factor: {real_time_factor}")

    # Sleep for a short duration before collecting the next set of metrics
    time.sleep(1)
    
    # Measure time taken for this step
    step_end_time = time.time()
    step_duration = step_end_time - step_start_time
    # Adjust simulation duration by the time taken for this step
    simulation_start_time += step_duration

# Write metrics to CSV file
with open('simulation_metrics.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'CPU Usage (%)', 'CPU Usage Per Core (%)', 'Memory Usage (%)', 'Memory Usage (MB)', 'GPU Utilization (%)', 'GPU Memory Usage (%)', 'GPU Memory Usage (MB)', 'FPS', 'Real-Time Factor'])
    for i in range(len(cpu_percentages)):
        writer.writerow([i+1, cpu_percentages[i], cpu_usages[i], memory_percentages[i], memory_usages[i], gpu_percentages[i], gpu_memory_percentages[i], gpu_memory_usages[i], fps_list[i], real_time_factors[i]])

print("Metrics have been saved to simulation_metrics.csv")