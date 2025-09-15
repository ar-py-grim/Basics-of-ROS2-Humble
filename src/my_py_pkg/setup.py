from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='grim',
    maintainer_email='grim@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_py_pkg.first_node:main",
            "robot_publisher = my_py_pkg.robot_publisher:main",
            "robot_subscriber = my_py_pkg.robot_subscriber:main",
            "number_publisher = my_py_pkg.number_publisher:main",
            "Addnum_server = my_py_pkg.Addnum_server:main",
            "Addnum_client = my_py_pkg.Addnum_client:main",
            "Hardware_publisher = my_py_pkg.Hardware_publisher:main",
            "battery_client = my_py_pkg.battery_client:main",
            "turtle_controller = my_py_pkg.turtle_controller:main",
            "turtle_spawner = my_py_pkg.turtle_spawner:main"
        ],
    },
)
