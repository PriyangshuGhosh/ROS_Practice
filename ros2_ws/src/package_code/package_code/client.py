#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv._add_two_ints import AddTwoInts
from functools import partial

class MyNode(Node):
    def __init__(self):
        super().__init__("client_add_two_ints")
        self.client_= self.create_client(AddTwoInts,"add_two_ints")

    def call_add_two_ints(self,x,y):
        while not self.client_.wait_for_service(2.0):
            self.get_logger().warn("Waiting for server to get online")
        request=AddTwoInts.Request()
        request.a=x
        request.b=y
        future = self.client_.call_async(request)
        future.add_done_callback(partial(self.callback_add_two_ints,request=request))
    def callback_add_two_ints(self, future, request):
        response=future.result()
        self.get_logger().info(f"reveived response {request.a}+{request.b} = {response.sum}")



def main(args=None):
    rclpy.init(args=args)
    node=MyNode()
    node.call_add_two_ints(3,4)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


