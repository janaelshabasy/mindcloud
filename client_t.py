import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from turtlesim.srv import TeleportAbsolute
import threading
import math
class Client(Node):
    def __init__(self):
        super().__init__("client_turtle")
        self.vel_publisher = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.client = self.create_client(TeleportAbsolute, "/turtle1/teleport_absolute")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for teleport service...")
        self.current_pose = None
        self.input_thread = threading.Thread(target=self.get_input, daemon=True)
        self.input_thread.start()
    
    def get_input(self):
        while rclpy.ok():
            input_x= float(input("enter x: ").strip())
            input_y= float(input("enter y: ").strip())
            if input_x <=11.0 and input_y <=11.0 and input_x>=0 and input_y>=0:
                request = TeleportAbsolute.Request()
                request.x = input_x
                request.y = input_y
                self.client.call_async(request)
            else:
                self.get_logger().info("out of boundaries")
def main(args=None):
    rclpy.init(args=args)
    node=Client()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()