import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from custom_action_interfaces.action import Fibonacci

class MyActionClientNode(Node):
    def __init__(self):
        super().__init__("action_client_node")
        self.action_client_ = ActionClient(self, Fibonacci, "fibonacci")

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self.action_client_.wait_for_server()

        self.send_goal_future = self.action_client_.send_goal_async(goal_msg, feedback_callback = self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal Rejected :(")
            return
        self.get_logger().info("Goal Accepted :)")

        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info("Result: {0}".format(result.sequence))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info("Received feedback : {0}".format(feedback.partial_sequence))


def main():
    rclpy.init()
    node = MyActionClientNode()
    node.send_goal(10)
    rclpy.spin(node)

if __name__ == "__main__":
    main()