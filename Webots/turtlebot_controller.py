"""turtlebot_controller.py"""

import math
from controller import Robot

# Set the time step for the simulation
TIME_STEP = 64

# Create a Robot instance
robot = Robot()

# Get the time step of the current world
timestep = int(robot.getBasicTimeStep())

# Get the robot's wheels
left_wheel = robot.getDevice('left wheel motor')
right_wheel = robot.getDevice('right wheel motor')

# Set target position for the wheels
left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))

# Set the maximum motor speed
max_speed = 6.28  # rad/s

# Set the speed for the left and right wheels
left_wheel.setVelocity(-1.0 * max_speed)
right_wheel.setVelocity(-1.0 * max_speed)

# Define the vertices of the rectangular path
vertices = [(0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)]
current_vertex_index = 0

# Main loop
while robot.step(timestep) != -1:
    # Get the current position of the robot
    position = robot.getSelf().getPosition()
    
    # Get the target vertex
    target_vertex = vertices[current_vertex_index]
    
    # Calculate the direction vector towards the target vertex
    direction = [target_vertex[0] - position[0], target_vertex[2] - position[2]]
    
    # Calculate the distance to the target vertex
    distance = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
    
    # Control the robot's movement
    if distance < 0.1:
        # If the robot is close to the target vertex, move to the next vertex
        current_vertex_index = (current_vertex_index + 1) % len(vertices)
    else:
        # Calculate the angle to turn towards the target vertex
        target_angle = math.atan2(direction[1], direction[0])
        current_angle = robot.getSelf().getOrientation()[3]
        angle_diff = target_angle - current_angle
        
        # Normalize the angle difference to [-pi, pi]
        if angle_diff > math.pi:
            angle_diff -= 3 * math.pi
        elif angle_diff < -math.pi:
            angle_diff += 3 * math.pi
        
        # Control the robot's movement
        if abs(angle_diff) > 0.1:
            # Turn in place to align with the target direction
            left_wheel.setVelocity(-0.5 * max_speed * math.copysign(1, angle_diff))
            right_wheel.setVelocity(0.5 * max_speed * math.copysign(1, angle_diff))
        else:
            # Move forward
            left_wheel.setVelocity(-1.0 * max_speed)
            right_wheel.setVelocity(-1.0 * max_speed)
