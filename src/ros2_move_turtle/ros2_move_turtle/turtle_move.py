import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtleMove(Node):

    def __init__(self):
        super().__init__('turtle_move')

        # Suscripcion
        self.subscription = self.create_subscription(
            Pose,
            '/turtle_1/pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        # Publicacion
        self.publisher_ = self.create_publisher(Twist, '/turtle_1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0


    def listener_callback(self, msg):
        self.get_logger().info(f'Received pose: x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f}')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x, msg.linear.y, msg.angular.z = 1.0, 0.0, 0.5
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: linear.x={msg.linear.x}, linear.y={msg.linear.y}, angular.z={msg.angular.z}')
        self.i += 1


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