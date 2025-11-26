#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv._set_bool import SetBool
from functools import partial

class Client(Node):
    def __init__(self):
        super().__init__("reset_counter")
        self.client_= self.create_client(SetBool,"reset_counter")

    def init_counter(self):
        while not self.client_.wait_for_service(2.0):
            self.get_logger().warn("Waiting for server to get online")
        request=SetBool.Request()
        request.data = True
        future = self.client_.call_async(request)
        future.add_done_callback(partial(self.callback_reset,request=request))
    def callback_reset(self, future, request):
        response=future.result()
        if response.success:
            self.get_logger().info(f"reveived response  = {response.success}")
        else :
            self.get_logger().info(f"reveived response  = {response.success}")




def main(args=None):
    rclpy.init(args=args)
    node=Client()
    node.init_counter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


