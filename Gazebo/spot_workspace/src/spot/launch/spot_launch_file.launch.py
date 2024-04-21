import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument,ExecuteProcess,IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration,Command,PythonExpression
from launch_ros.actions import Node
from launch.conditions import UnlessCondition,IfCondition
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    robot_name_in_model = 'spot'
    package_name = 'spot'


    

    urdf_file_name = 'spot_model.urdf'
    urdf_path = os.path.join(
        get_package_share_directory('spot'),'urdf',urdf_file_name)
    
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()
    
    pkg_gazebo_ros = FindPackageShare(package='gazebo_ros').find('gazebo_ros')   
    pkg_share = FindPackageShare(package=package_name).find(package_name)

    # # Launch Gazebo
    # gazebo_node = ExecuteProcess(
    #         cmd=['gazebo'],
    #         output='screen')

    # Pose where we want to spawn the robot
    spawn_x_val = '0.0'
    spawn_y_val = '0.0'
    spawn_z_val = '0.0'
    spawn_yaw_val = '0.00'


    launch_description = LaunchDescription()




    urdf_model = LaunchConfiguration('urdf_model')

    declare_urdf_model_path_cmd = DeclareLaunchArgument(
    name='urdf_model', 
    default_value=urdf_path, 
    description='Absolute path to robot urdf file')

    # Subscribe to the joint states of the robot, and publish the 3D pose of each link.    
    start_robot_state_publisher_cmd = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    parameters=[{'robot_description': robot_desc}],)



    # Start Gazebo server
    start_gazebo_server_cmd = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')),
    )
 
  # Start Gazebo client    
    start_gazebo_client_cmd = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')),
   )
 
  # Launch the robot
    spawn_entity_cmd = Node(
    package='gazebo_ros', 
    executable='spawn_entity.py',
    arguments=['-entity', robot_name_in_model, 
                '-topic', 'robot_description',
                    '-x', spawn_x_val,
                    '-y', spawn_y_val,
                    '-z', spawn_z_val,
                    '-Y', spawn_yaw_val],
                    output='screen') 


    launch_description.add_action(declare_urdf_model_path_cmd)

    launch_description.add_action(start_gazebo_server_cmd)
    launch_description.add_action(start_gazebo_client_cmd)
    launch_description.add_action(spawn_entity_cmd)
    launch_description.add_action(start_robot_state_publisher_cmd)
   
    
    return launch_description

    #return LaunchDescription([
     #   gazebo_node,
      #  gazebo_ros2_control_node,
       # spawn_entity_node
    #])

if __name__ == '__main__':
    generate_launch_description()

