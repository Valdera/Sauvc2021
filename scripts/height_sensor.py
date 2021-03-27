#!/usr/bin/env python
"""
Kodingan untuk memberikan state kedalaman pada ROV
"""

import ms5837
import time
import rospy
from std_msgs.msg import Float64

sensor = ms5837.MS5837_02BA(1) # Default I2C bus is 1 (Raspberry Pi 3)


if __name__ == '__main__':
    rospy.init_node('height_sensor', anonymous=True)
    state_publisher = rospy.Publisher("/height_controller/state", Float64, queue_size=8)

    # inisialisasi
    if not sensor.init():
        print("Sensor could not be initialized")
        exit(1)

    while not rospy.is_shutdown():
        if sensor.read():
            state = Float64()
            state.data = sensor.pressure()
            state_publisher.publish(state)
        else:
            print("Sensor read failed!")
            exit(1)