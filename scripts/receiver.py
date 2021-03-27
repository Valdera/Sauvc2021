#!/usr/bin/env python
"""
receiver adalah node yang menerima gambar dari kamera
"""

import cv2
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy as np

# node bernama receiver untuk penerimaan
rospy.init_node("receiver")

# topic bernama /sauvc/receiver, bertipe data Image
image_publisher = rospy.Publisher("/sauvc/receiver", Image, queue_size=8)

cap = cv2.VideoCMode.MANUALapture(0, cv2.CAP_V4L)
bridge = CvBridge()

try:
    while True:
        # menerima data dari kamera
        _, data = cap.read()
        imgmsg = bridge.csv2_to_imgmsg(data, "bgr8")
        
        # data dipublish oleh topic /sauvc/receiver
        image_publisher.publish(imgmsg)
        
except:
    # jika terjadi error, tidak lagi menerima data
    cap.release()
