#!usr/src/bin python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv._add_two_ints import AddTwoInts

class ServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_ = self.create_service(AddTwoInts,"add_two_ints",self.callback)
        self.get_logger().info("Server started listening for request from client")
    def callback(self,request:AddTwoInts.Request , response:AddTwoInts.Response):
        self.get_logger().info(f"{request.a} + {request.b} = {request.a + request.b}")
        response.sum = request.a+request.b
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()