# Project Status Report -1 - Comparing Coppelia SIM , Webots and Gazebo for ROS models

## Summary 


Our project is aimed towards comparing the efficacy of different simulators like Coppelia SIM , Gazebo and Webots for different robotic models. The aim is to compare their performance in simulating robotic systems, assessing qualitative and quantitative factors that will allow us to gauge how each of these simulators support robots of different use cases. For example, if we consider an object moving in an environment with obstacles Coppelia SIM with its realistic physics engine can simulate almost close simulations of real time scenario of the object's motion. On the other hand, Gazebo will allow more realistic and accurate collisions at run time. Webots generally renowned for simulating swarm robots can give a generalistic real time simulation of the system. Our goal is to establish a comparision between such simulators and reach towards establishing a universal metric for this comparision. 

Continuing with our goal of the project, we stretched our goals to even further to bring in context to comparison of the simulators. We have now integrated a chatbot leveraging the power of LLM and Langchain models. We have trained the chatbot using the data that we collected. We are sure that this chatbot - SimBot will aid the budding developers like us in giving a headstart to their journey in the field of robotics.


Configuring the chatbot: 


## Installation

To install the required dependencies, run the following command:


``` pip install -r requirements.txt ```

## To start the streamlit server

``` streamlit run simulator_chatbot.py ```


## You can find the chatbot running on : http://localhost:8501/








