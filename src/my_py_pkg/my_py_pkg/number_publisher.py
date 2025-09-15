#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class number_publishNode(Node): 
    def __init__(self):
        super().__init__("number_publish") 

        # name of parameter + default value
        self.declare_parameter("number_to_publish",28)
        self.declare_parameter("publish_frequency",1.0)

        # now get value of parameter from terminal
        self.number = self.get_parameter("number_to_publish").value
        self.publish_frequency = self.get_parameter("publish_frequency").value  

        self.publisher_ = self.create_publisher(Int64,"number",10)
        self.timer_ = self.create_timer(1.0/self.publish_frequency,self.publish_number)
        self.get_logger().info("Transmission has begun")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = number_publishNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
