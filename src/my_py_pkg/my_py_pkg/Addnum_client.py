#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddNumClientNode(Node): 
    def __init__(self):
        super().__init__("AddNumClient") 

        # we can server multiple times
        self.callbacksumclient(8,45)   
        self.callbacksumclient(248,15)
        self.callbacksumclient(35,64)  

    def callbacksumclient(self,a,b):
        client = self.create_client(AddTwoInts,"AddNum") 

       # in case server is not ready before client, client has to wait till that time
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for server....")

        # create a request object
        request = AddTwoInts.Request() 
        request.a = a
        request.b = b

        ''' in asynch call a request will be sent to server every specified 
        time but the program will not be blocked indefinitely '''
        future = client.call_async(request)

        ''' to add more parameters to this callback function we use partial
            we need to pass the arguments in this function same order as in callback_future
            in a=a and b=b left side "a" is from callback_future function while right side "a" is from callbacksumclient func.'''
        future.add_done_callback(partial(self.callback_future,a=a,b=b))

    def callback_future(self,future,a,b):
        try:
            response=future.result()
            self.get_logger().info(f"{a} + {b} = {response.sum}")

        except Exception as e:
            self.get_logger().error(f"Service called failed {e}")

def main(args=None):
    rclpy.init(args=args)
    node = AddNumClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()