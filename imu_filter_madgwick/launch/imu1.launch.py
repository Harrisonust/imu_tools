import os
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_dir = os.path.join(get_package_share_directory('imu_filter_madgwick'), 'config')

    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package='imu_filter_madgwick',
                executable='imu_filter_madgwick_node',
                name='imu_filter_madgwick1',
                output='screen',
                parameters=[
                    os.path.join(config_dir, 'imu_filter.yaml'),
                    {'use_mag': False},
                    {'fixed_frame': "imu1"},
                ],
                remappings=[
                    ("/imu/data_raw", "/Imu1/Raw"),
                    ("/imu/mag", "/Imu1/Mag"),
                    ("/imu/data", "/Imu1")
                ]
            )
        ]
    )
