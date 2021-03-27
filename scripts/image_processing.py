#!/usr/bin/env python
"""
untuk mendeteksi gambar dari misi 1
"""

import cv2
import numpy as np
import rospy
from std_msgs.msg import Bool, Float64
from sauvc2021.msg import Misi
from sensor_msgs.msg import Image
from image_processing_lib import *

currentMisi = Misi()


# For object detection
def misiCallback(msg):
    currentMisi.data = msg.data
   
def imageCallback(frame):
    is_detected = Bool()
    state = Float64()
    state_coor = tuple()

    if currentMisi.data is Misi.MISI_1:
        state_coor, is_detected.data = misi1.image_process_misi1(frame)
    elif currentMisi.data is Misi.MISI_2:
        state_coor, is_detected.data = misi2.image_process_misi2(frame)
    elif currentMisi.data is Misi.MISI_3:
        state_coor, is_detected.data = misi3.image_process_misi3(frame)
    
    state.data = state_coor[0]
    is_detected_publisher.publish(is_detected)
    state_publisher.publish(state)

        

if __name__ == '__main__':
    rospy.init_node('image_processing')

    # PUBLISHER    
    is_detected_publisher = rospy.Publisher('/sauvc/is_detected', Bool, queue_size=8) 
    state_publisher = rospy.Publisher('/coor_controller/state', Float64, queue_size=8) 

    # SUBSRIBER
    misi_subscriber = rospy.Subscriber('/sauvc/misi', Misi, misiCallback)    
    image_subscriber = rospy.Subscriber('/sauvc/receiver', Image, imageCallback) 
    
    
    