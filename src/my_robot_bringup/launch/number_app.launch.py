from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    number_publisher_node = Node(
        package = "my_py_pkg",
        executable = "number_publisher",

        # to rename name of node during run time
        name = "my_number_publisher",

        # to rename topic name
        remappings=[
            ("number","my_number")
        ],

        # to set values of the parameters
        parameters=[
            {"number_to_publish": 69},
            {"publish_frequency": 5.0}
            ]
    )

    counter_subscriber_node = Node(
        package = "my_cpp_pkg",
        executable = "number_counter",

        # to rename name of node during run time
        name = "my_counter_subscriber",

        # to rename topic name
         remappings=[
            ("number_count","my_number_count"),
            ("number","my_number")
        ]
    )

    # launch publisher_node
    ld.add_action(number_publisher_node)

    # launch subscriber node
    ld.add_action(counter_subscriber_node)
    return ld