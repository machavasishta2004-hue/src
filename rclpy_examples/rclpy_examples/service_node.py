import rclpy 
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MyClientNode(Node):
    def __init__(self):
        super().__init__("service_node")
        self.get_logger().info("Starting my first service node")
        self.client_ = self.create_service(
            AddTwoInts, "add_two_ints", self.add_two_ints_callback)
    
    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info("Adding two integers-->a: %d, b: %d" %(request.a, request.b))

        return response

def main():
    rclpy.init()
    node=MyClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()