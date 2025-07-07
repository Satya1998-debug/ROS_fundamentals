from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()
    
    # Get the package share directory for 'robo_bringup'
    parameters_file = os.path.join(get_package_share_directory('robo_bringup'), 'config', 'number.yaml')

    # these node objects are for launching not related to actual nodes in the package
    # they are just for the sake of this example to show how to launch multiple nodes
    number_publisher = Node(
        package='ros_basics',
        executable='number_publisher',
        name='my_number_publisher',
        output='screen',
        remappings=[('/number', '/my_number')],
        parameters=[
            {"number": 6},
            {"timer_period": 2.0}
        ]
    )

    number_counter = Node(
        package='ros_basics',
        executable='number_counter',
        name='my_number_counter',
        output='screen'
    )
    
    number_counter = Node(
        package='ros_basics',
        executable='number_counter',
        name='my_number_counter',
        output='screen',
        remappings=[('/number', '/my_number')]
    )

    ld.add_action(number_publisher)
    ld.add_action(number_counter)

    return ld