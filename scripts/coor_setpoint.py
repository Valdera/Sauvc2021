#!/usr/bin/env python
"""
Kodingan untuk mengatur setpoint horizontal
"""

import rospy
from std_msgs.msg import Float64, Int16
from sauvc2021.msg import Mode

setpoint_coor = Float64()

if __name__ == '__main__':
    rospy.init_node('coor_setpoint')

    setpoint_coor.data = 320 

    # Set Publisher
    setpoint_publisher = rospy.Publisher("/coor_controller/setpoint", Float64, queue_size=14)

    # While still alive
    while not rospy.is_shutdown():
        setpoint_publisher.publish(setpoint_coor)
        rospy.spinOnce()