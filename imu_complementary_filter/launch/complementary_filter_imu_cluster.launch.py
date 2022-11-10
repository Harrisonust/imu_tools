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
                        get_package_share_directory('imu_complementary_filter'),
                        'launch/complementary_filter_imu0.launch.py'))
            ), 
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('imu_complementary_filter'),
                        'launch/complementary_filter_imu1.launch.py'))
            ), 
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('imu_complementary_filter'),
                        'launch/complementary_filter_imu2.launch.py'))
            )
        ]
    )
