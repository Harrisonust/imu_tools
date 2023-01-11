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
                name='imu_filter_madgwick2',
                output='screen',
                parameters=[
                    os.path.join(config_dir, 'imu_filter.yaml'),
                    {'use_mag': False},
                    {'publish_tf': False},
                ],
                remappings=[
                    ("/imu/data_raw", "/Imu2/Raw"),
                    ("/imu/mag", "/Imu2/Mag"),
                    ("/imu/data", "/Imu2")
                ]
            )
        ]
    )

