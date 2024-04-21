#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

# Define global variables for key mappings
key_mapping = {'w': [1.0, 0.0, 0.0, 0.0],   # Move forward
               's': [-1.0, 0.0, 0.0, 0.0],  # Move backward
               'a': [0.0, 1.0, 0.0, 0.0],   # Turn left
               'd': [0.0, -1.0, 0.0, 0.0],  # Turn right
               'q': [0.0, 0.0, 0.0, 1.0],   # Rotate left
               'e': [0.0, 0.0, 0.0, -1.0],  # Rotate right
               'stop': [0.0, 0.0, 0.0, 0.0]} # Stop

def on_press(key):
    global twist_pub
    try:
        twist = Twist()
        if key.char in key_mapping:
            twist.linear.x = key_mapping[key.char][0]
            twist.linear.y = key_mapping[key.char][1]
            twist.angular.z = key_mapping[key.char][3]
            twist_pub.publish(twist)
        elif key.char == 'q':
            twist.angular.z = key_mapping[key.char][3]
            twist_pub.publish(twist)
        elif key.char == 'e':
            twist.angular.z = key_mapping[key.char][3]
            twist_pub.publish(twist)
        elif key.char == ' ':
            twist = Twist()  # Stop the robot
            twist_pub.publish(twist)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def rover_control():
    global twist_pub
    rospy.init_node('rover_keyboard_control', anonymous=True)
    twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    rospy.spin()

if __name__ == '__main__':
    try:
        rover_control()
    except rospy.ROSInterruptException:
        pass