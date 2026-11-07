import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__("publisher_node")
        self.publisher_ = self.create_publisher(String, "topic", 10)
        self.get_logger().info("My first publisher node has started")
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = str("Hello World " + str(self.i))
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing : " + msg.data)
        self.i += 1




def main(args=None):
    rclpy.init(args=args)
    node=PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()