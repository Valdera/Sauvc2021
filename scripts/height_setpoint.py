#!/usr/bin/env python
"""
Kodingan untuk mengatur setpoint vertical
"""

import rospy
from std_msgs.msg import Float64, Int16
from sauvc2021.msg import Mode

setpoint_height = Float64()

if __name__ == '__main__':
    rospy.init_node('height_setpoint')

    setpoint_height.data = 50

    # Set Publisher
    setpoint_publisher = rospy.Publisher("/height_controller/setpoint", Float64, queue_size=14)
    
    # While still alive
    while not rospy.is_shutdown():
        setpoint_publisher.publish(setpoint_height)
        rospy.spinOnce()