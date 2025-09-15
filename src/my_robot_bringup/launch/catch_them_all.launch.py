from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    # turtlesim node 
    turtlesim_node  = Node(
        package = "turtlesim",
        executable = "turtlesim_node"
    )

    # spawner node 
    turtle_spawner_node = Node(
        package = "my_py_pkg",
        executable = "turtle_spawner",
        parameters=[
            {"spawn_frequency": 1.0},
            {"turtle_name_prefix": "turtle"}
        ]
    )
   
    # controller node
    turtle_controller_node = Node(
        package = "my_py_pkg",
        executable = "turtle_controller",
         parameters=[
            {"catch_closest_turtle_first": True}
        ]
    )

    # launch turtlesim node
    ld.add_action(turtlesim_node)

    # launch spawner node 
    ld.add_action(turtle_spawner_node)

    # launch controller node 
    ld.add_action(turtle_controller_node)

    return ld
