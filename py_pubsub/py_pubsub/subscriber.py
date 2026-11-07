import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MySubcriberNode(Node):
    def __init__(self):
        super().__init__("subscriber_node")
        self.subscriber_ = self.create_subscription(
            String, "topic", self.listener_callback, 10)
        
    def listener_callback(self, msg: String):
        self.get_logger().info("I heard : " + msg.data)




def main(args=None):
    rclpy.init(args=args)
    node=MySubcriberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()