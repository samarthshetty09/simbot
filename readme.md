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
    * Simulation of Turtle Bot in Webots : [Youtube Link]([https://www.youtube.com/watch?v=Kr2a7oU1kHg](https://youtu.be/Kr2a7oU1kHg))

* #### Sai Krishna Rajaraman - Coppelia SIM

* #### Samarth Shetty - Gazebo 

## Next Steps

* #### Sri Roopa Ramesh Babu - Webots
    * Next step is to simulate high level robotic models. 
    * Compare the Simulators across different operating Systems.
    * Visualize the Inferences across different simulators.
* #### Sai Krishna Rajaraman - Coppelia SIM
* #### Samarth Shetty - Gazebo 
