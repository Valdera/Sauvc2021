#!/usr/bin/env python
"""
untuk menggerakkan motor secara manual
"""

import rospy
from std_msgs.msg import Bool, Float64
from sauvc2021.msg import Misi, Mode
from mavros_msgs.msg import OverrideRCIn
from sensor_msgs.msg import Joy

mode = Mode()


def driverCallback(msg):
    global mode
    arr = msg.mode
    # Ganti mode sesuai mode sekarang 
    mode.data = arr[0]
                

# Untuk manjalankan motor dengan joystic
def joyCallback(msg):
    global mode
    if (mode.data != Mode.MANUAL):
        return
    if (msg.buttons[0] == 1):
        rcin = OverrideRCIn()
        rcin.channels[0] = 1600
        rcin.channels[1] = 1600
        rcin.channels[2] = 1600
        rcin.channels[3] = 1600
        motor_publisher.publish(rcin)
        rospy.loginfo("lurus")
    elif (msg.buttons[1] == 1):
        rcin = OverrideRCIn()
        rcin.channels[0] = 1600
        rcin.channels[1] = 1400
        rcin.channels[2] = 1600
        rcin.channels[3] = 1400
        motor_publisher.publish(rcin)
        rospy.loginfo("Geser kanan")
    elif (msg.buttons[3] == 1):
        rcin = OverrideRCIn()
        rcin.channels[0] = 1400
        rcin.channels[1] = 1600
        rcin.channels[2] = 1400
        rcin.channels[3] = 1600
        motor_publisher.publish(rcin)
        rospy.loginfo("Geser kiri")
    elif (msg.axes[0] == -1 and msg.axes[2] == -1):
        rcin = OverrideRCIn()
        rcin.channels[0] = 1600
        rcin.channels[1] = 1400
        rcin.channels[2] = 1400
        rcin.channels[3] = 1600
        motor_publisher.publish(rcin)
        rospy.loginfo("Putar Kanan")
    elif (msg.axes[0] == 1 and msg.axes[2] == 1):
        rcin = OverrideRCIn()
        rcin.channels[0] = 1400
        rcin.channels[1] = 1600
        rcin.channels[2] = 1600
        rcin.channels[3] = 1400
        motor_publisher.publish(rcin)
        rospy.loginfo("Putar Kiri")
    elif (msg.buttons[1] == -1):
        rcin = OverrideRCIn()
        rcin.channels[4] = 1600
        rcin.channels[5] = 1600
        motor_publisher.publish(rcin)
        rospy.loginfo("Tenggelam")
    elif (msg.buttons[1] == 1):
        rcin = OverrideRCIn()
        rcin.channels[4] = 1400
        rcin.channels[5] = 1400
        motor_publisher.publish(rcin)
        rospy.loginfo("Angkat")
    else:
        rcin = OverrideRCIn()
        rcin.channels[0] = 1500
        rcin.channels[1] = 1500
        rcin.channels[2] = 1500
        rcin.channels[3] = 1500
        motor_publisher.publish(rcin)
        rospy.loginfo("Diem")

if __name__ == '__main__':
    rospy.init_node('motor_controller_manual')

    # SUBSCRIBER
    joy_subscriber = rospy.Subscriber('joy', Joy, joyCallback)

    # PUBLISHER
    motor_publisher = rospy.Publisher("/mavros/rc/override", OverrideRCIn, queue_size=8)
    rospy.spin()