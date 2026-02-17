import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class TurtleMove(Node):

    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            '/chatter',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    turtle_move = TurtleMove()

    rclpy.spin(turtle_move)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_move.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()