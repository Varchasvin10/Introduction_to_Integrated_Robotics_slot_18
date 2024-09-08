import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='iir').find('iir')
    default_model_path = os.path.join(pkg_share, 'description/iir_description.urdf')
    world_path=os.path.join(pkg_share, 'world/my_world.sdf')

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
    )
    gazebo_start = launch.actions.ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path], output='screen')
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
  	executable='joint_state_publisher',
  	name='joint_state_publisher',
  	arguments=[default_model_path], #Add this line
    )
    spawn_entity = launch_ros.actions.Node(
     package='gazebo_ros',
     executable='spawn_entity.py',
     arguments=['-entity', 'iir', '-topic', 'robot_description'],
     output='screen'
    )
    robot_localization_node = launch_ros.actions.Node(
     package='robot_localization',
     executable='ekf_node',
     name='ekf_filter_node',
     output='screen',
     parameters=[os.path.join(pkg_share, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='True',
                                            description='Flag to enable use_sim_time'),
	gazebo_start,
        joint_state_publisher_node,
        robot_state_publisher_node,
        spawn_entity,
   ])
