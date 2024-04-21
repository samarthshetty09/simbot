"""turtle_controller controller."""

from controller import Supervisor
import csv
import psutil
import time

# Initialize the Supervisor
supervisor = Supervisor()

# Time step (duration of each simulation step, typically corresponds to your world's basicTimeStep)
time_step = int(supervisor.getBasicTimeStep())

# Function to get CPU usage
def get_cpu_metrics():
    cpu_percent = psutil.cpu_percent(interval=None)  # Get instant CPU percent
    cpu_usage = sum(psutil.cpu_percent(interval=None, percpu=True))
    return cpu_percent, cpu_usage

# Function to get memory usage
def get_memory_metrics():
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    memory_usage = memory_info.used / (1024 ** 2)  # Convert to MB
    return memory_percent, memory_usage

# Define simulation duration (in simulation steps)
simulation_duration = 60 # Adjust this based on your desired simulation duration in steps

# Initialize lists to store metrics
cpu_percentages = []
total_cpu_usages = []
memory_percentages = []
memory_usages = []
fps_list = []
real_time_factors = []

# Main simulation loop
start_real_time = time.time()
for i in range(simulation_duration):
    if supervisor.step(time_step) == -1:
        break
    
    # Get CPU and memory metrics
    cpu_percent, total_cpu_usage = get_cpu_metrics()
    memory_percent, memory_usage = get_memory_metrics()
    
    # Store metrics
    cpu_percentages.append(cpu_percent)
    total_cpu_usages.append(total_cpu_usage)
    memory_percentages.append(memory_percent)
    memory_usages.append(memory_usage)
    
    # Calculate FPS and Real-Time Factor
    elapsed_real_time = time.time() - start_real_time
    if elapsed_real_time > 0:
        fps = i / elapsed_real_time
        real_time_factor = (i * time_step / 1000.0) / elapsed_real_time
    else:
        fps = 0
        real_time_factor = 0
    
    fps_list.append(fps)
    real_time_factors.append(real_time_factor)
    
    # Print metrics to console
    print(f"Step: {i}, CPU Usage: {cpu_percent}%, Total CPU Usage: {total_cpu_usage} MB, Memory Usage: {memory_percent}%, Memory Usage: {memory_usage} MB, FPS: {fps:.2f}, Real-Time Factor: {real_time_factor:.2f}")

# Write metrics to CSV file
with open('simulation_metrics.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Step', 'CPU Usage (%)', 'Total CPU Usage (MB)', 'Memory Usage (%)', 'Memory Usage (MB)', 'FPS', 'Real-Time Factor'])
    for i in range(len(cpu_percentages)):
        writer.writerow([i, cpu_percentages[i], total_cpu_usages[i], memory_percentages[i], memory_usages[i], fps_list[i], real_time_factors[i]])

print("Metrics have been saved to simulation_metrics.csv")

