cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
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

add_executable(cpp_node src/first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(robot_subscriber src/robot_subscriber.cpp)
ament_target_dependencies(robot_subscriber rclcpp example_interfaces)

add_executable(robot_publisher src/robot_publisher.cpp)
ament_target_dependencies(robot_publisher rclcpp example_interfaces)

add_executable(number_counter src/number_counter.cpp)
ament_target_dependencies(number_counter rclcpp example_interfaces)

add_executable(Addnum_server src/Addnum_server.cpp)
ament_target_dependencies(Addnum_server rclcpp example_interfaces)

add_executable(Addnum_client src/Addnum_client.cpp)
ament_target_dependencies(Addnum_client rclcpp example_interfaces)

add_executable(Hardware_publisher src/Hardware_publisher.cpp)
ament_target_dependencies(Hardware_publisher rclcpp my_robot_interfaces)

add_executable(ledpanel_server src/ledpanel_server.cpp)
ament_target_dependencies(ledpanel_server rclcpp my_robot_interfaces)

install(TARGETS
cpp_node
robot_subscriber
robot_publisher
number_counter
Addnum_server
Addnum_client
Hardware_publisher
ledpanel_server
DESTINATION  lib/${PROJECT_NAME})

ament_package()
