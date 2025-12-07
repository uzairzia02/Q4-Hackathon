import pytest
import rclpy
from std_msgs.msg import String
import threading
import time

from code_examples.ros2.module1.simple_publisher import SimplePublisher

@pytest.fixture(scope='module')
def ros_node():
    rclpy.init()
    node = SimplePublisher()
    yield node
    node.destroy_node()
    rclpy.shutdown()

def test_simple_publisher_publishes_messages(ros_node):
    # Create a subscriber to listen for messages
    messages_received = []
    subscriber = ros_node.create_subscription(
        String,
        'topic',
        lambda msg: messages_received.append(msg.data),
        10
    )

    # Spin the node in a separate thread to allow message processing
    spin_thread = threading.Thread(target=rclpy.spin, args=(ros_node,))
    spin_thread.start()

    # Wait for a few messages to be published
    time.sleep(2)

    # Stop spinning and destroy the subscriber
    ros_node.destroy_subscription(subscriber)
    rclpy.spin_once(ros_node, timeout_sec=0.1) # Process any remaining messages
    spin_thread.join(timeout=1) # Wait for the spin thread to finish

    # Assert that messages were received
    assert len(messages_received) > 0
    assert "Hello ROS 2" in messages_received[0]
