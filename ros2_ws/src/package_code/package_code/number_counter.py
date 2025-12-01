import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv._set_bool import SetBool

class number_conunter(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.count_=0
        self.subscriber_=self.create_subscription(Int64,"number",self.caller,1)
        self.publisher_=self.create_publisher(Int64,"number_count",9)
        self.service_=self.create_service(SetBool,"reset_counter",self.callback)
        self.get_logger().info("Initialized number counter")

    def callback(self,request:SetBool.Request , response:SetBool.Response):
         self.get_logger().info(f"Received bool value {request.data}")
         if request.data:
            self.count_ = 0
            response.success = True 
            response.message = "Counter reset"
         else:
            response.success = False
            response.message = "Failed to reset counter"
         return response
             

    def caller(self , msg: Int64):
        if msg.data:
            pub=Int64()
            self.count_+=msg.data
            pub.data = self.count_
            self.get_logger().info(f"Received data from the topic number :{msg.data}")
            self.publisher_.publish(pub)
            self.get_logger().info(f"Published data into the topic number_count :{self.count_}")
    


def main(args=None):
    rclpy.init(args=args)
    node = number_conunter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()