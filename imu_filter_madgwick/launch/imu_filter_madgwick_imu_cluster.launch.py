from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():
    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('imu_filter_madgwick'),
                        'launch/imu_filter_madgwick_imu0.launch.py'))
            ), 
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('imu_filter_madgwick'),
                        'launch/imu_filter_madgwick_imu1.launch.py'))
            ), 
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('imu_filter_madgwick'),
                        'launch/imu_filter_madgwick_imu2.launch.py'))
            ),
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                name='tf2_ros0', 
                arguments=['1', '1', '1', '0', '0', '0', 'palm', 'imu0']
            ),
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                name='tf2_ros2', 
                arguments=['-1', '-1', '1', '0', '0', '0', 'palm', 'imu2']
            ),
        ]
    )
