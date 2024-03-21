# Project Status Report -1 - Comparing Coppelia SIM , Webots and Gazebo for ROS models

## Summary 


Our project is aimed towards comparing the efficacy of different simulators like Coppelia SIM , Gazebo and Webots for different robotic models. The aim is to compare their performance in simulating robotic systems, assessing qualitative and quantitative factors that will allow us to gauge how each of these simulators support robots of different use cases. For example, if we consider an object moving in an environment with obstacles Coppelia SIM with its realistic physics engine can simulate almost close simulations of real time scenario of the object's motion. On the other hand, Gazebo will allow more realistic and accurate collisions at run time. Webots generally renowned for simulating swarm robots can give a generalistic real time simulation of the system. Our goal is to establish a comparision between such simulators and reach towards establishing a universal metric for this comparision.  


## Progress

* #### Sri Roopa Ramesh Babu - Webots
    * Explored the Webots Simulator Environment - the User Interface, ROS support, Nodes, Controllers, Object, Scene, World and PROTO format of environment description.
    * Set up a simple environment to navigate TurtleBot3 Burger robot in a square bounding within the environment.
    * Experimented with various metrics including rotation , translation of both : the whole turtle bot and the LIDAR sensing element respectively.
    * Studied the considered qualitative metrics for the Webots ecosystem.
    * Tracked the CPU and memory usage of this implementation on a Windows ecosystem.
    * Simulation of Turtle Bot in Webots : [Youtube Link](https://www.youtube.com/watch?v=Kr2a7oU1kHg](https://youtu.be/Kr2a7oU1kHg)

* #### Saikrishna Rajaraman - Coppelia SIM
   * Explored the tutorials of CoppeliaSim simulator environment - Learnt about the different tools , Models, Links , joints etc.
   * Experimented with the mobile and non-mobile off the shelf robots in CoppeliaSim
   * Loaded the turtlebot 2 URDF by referring the tutorials and played around with the properties of the turtle bot.
   * Made note of the qualitative metrics such as OS support, Models supports etc and made a tabular column to compare with the other simulators.
   * Simulated the turtlebot and made note of couple of quantitative metrics like CPU Consumption, Memory usage.
   * Simulation demo - [Turtlebot CoppeliaSim Simulation](https://youtu.be/XnH3cdLI9Hk)

* #### Samarth Shetty - Gazebo 

## Next Steps

* #### Sri Roopa Ramesh Babu - Webots
    * Next step is to simulate high level robotic models. 
    * Compare the Simulators across different operating Systems.
    * Visualize the Inferences across different simulators.
* #### Saikrishna Rajaraman - Coppelia SIM
    * Decide on the quantitative metrics to measure relevant to developer friendliness.
    * Collect data from 3 different OS and 3 different robots and average it across different systems.
    * Analyze the data collected and make a comprehensive analysis of the simulators. 
* #### Samarth Shetty - Gazebo 
