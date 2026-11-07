import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MyClientNode(Node):
    def __init__(self):
        super().__init__("client_node")
        self.client_ = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client_.wait_for_service(1.0):
            self.get_logger().info("Service not available, waiting...")
        self.request_ = AddTwoInts.Request()
    
    def send_request(self, a, b):
        self.request_.a = a
        self.request_.b = b
        return self.client_.call_async(self.request_)

def main():
    rclpy.init()
    client = MyClientNode()
    future = client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(client, future)
    response = future.result()
    client.get_logger().info("Adding two integers--> a: %d, b: %d, and the result is %d"
    %(int(sys.argv[1]), int(sys.argv[2]), response.sum))
    rclpy.shutdown()

if __name__ == "__main__":
    main()