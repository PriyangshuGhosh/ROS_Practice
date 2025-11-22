#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("TestNode1")
        self.Counter_=0
        self.create_timer(1.5,self.caller)
    def caller(self):
        self.get_logger().info("Hello "+str(self.Counter_))
        self.Counter_+=1

def main(args=None):
    rclpy.init(args=args)
    node=MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()



