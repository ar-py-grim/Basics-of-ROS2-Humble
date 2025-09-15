#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddNumNode(Node): 
    def __init__(self):
        super().__init__("AddNum") 
        self.server = self.create_service(AddTwoInts,"AddNum",self.callbacksum)
        self.get_logger().info("service has started")

    def callbacksum(self,request,response):
        response.sum = request.a +request.b
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = AddNumNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()