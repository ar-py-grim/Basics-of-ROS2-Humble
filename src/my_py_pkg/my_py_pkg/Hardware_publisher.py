#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HwstatuspublisherNode(Node): 
    def __init__(self):
        super().__init__("hw_status") 
        self.hardware_status_publisher = self.create_publisher(HardwareStatus,"hw_status",10)
        self.timer = self.create_timer(1.0,self.publish_status)
        self.get_logger().info(" publsiher is publishing :)")

    def publish_status(self):
        msg = HardwareStatus()
        msg.temperature = 49
        msg.are_motors_ready = True
        msg.debug_message = "Nothing special here"
        self.hardware_status_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = HwstatuspublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()