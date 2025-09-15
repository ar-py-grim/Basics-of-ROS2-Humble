cmake_minimum_required(VERSION 3.8)
project(ros2project_lvl_3)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(turtlesim REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(my_robot_interfaces REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

add_library(turtle_controller_component SHARED src/turtle_controller.cpp)
ament_target_dependencies(turtle_controller_component rclcpp rclcpp_action rclcpp_lifecycle
                          rclcpp_components turtlesim geometry_msgs my_robot_interfaces)
rclcpp_components_register_nodes(turtle_controller_component "turtle_controller::TurtleController")


add_library(turtlebot3_control_component SHARED src/turtlebot3_controller.cpp)
ament_target_dependencies(turtlebot3_control_component rclcpp rclcpp_action rclcpp_lifecycle
                          rclcpp_components geometry_msgs my_robot_interfaces)
rclcpp_components_register_nodes(turtlebot3_control_component "turtlebot3_controller::TurtleBot3Controller")


install(TARGETS
  turtle_controller_component
  turtlebot3_control_component
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

ament_package()
