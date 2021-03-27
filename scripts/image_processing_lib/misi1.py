#!/usr/bin/env python
import cv2
import numpy as np

def image_process_misi1(frame):
    is_detected = False

     # Meresize state untuk ditampilkan si GUI
    img = cv2.resize(frame, None, fx = .3, fy = .3, interpolation = cv2.INTER_CUBIC)

    # Initialisasi state
    state_tuple = (img.shape[0]/2, img.shape[1]/2)
    state = Float64()

    # Mengubah gambar dari BGR menjadi HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (5, 5), 1)

    mask1 = cv2.inRange(hsv, (60.875, 140.25, 23.5), (150.875, 230.25, 113.5))
    mask2 = cv2.inRange(hsv, (58.6875, 230.75, 128.5), (98.6875, 270.75, 168.5))

    ret,thresh1 = cv2.threshold(mask1, 40, 255, cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(mask2, 40, 255, cv2.THRESH_BINARY)
    
    mask = cv2.bitwise_or(mask1, mask2)

    ret,thresh_final = cv2.threshold(mask, 40, 255, cv2.THRESH_BINARY)

    red_coor = None
    yellow_coor = None
    state_coor = (img.shape[0]/2, img.shape[1]/2) 

    contours_1, _= cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours_1) != 0:
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,0), 2)
        tengah_x = x + (w // 2)
        tengah_y = y + (h // 2 )
        cv2.circle(img, (tengah_x, tengah_y), 10, (0, 255, 0), -1)
        red_coor = (tengah_x, tengah_y)

    contours_2, _= cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours_2) != 0:
        c = max(contours_2, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,0), 2)
        tengah_x = x + (w // 2)
        tengah_y = y + (h // 2 )
        cv2.circle(img, (tengah_x, tengah_y), 10, (0, 255, 0), -1)
        yellow_coor = (tengah_x, tengah_y)

    if(len(contours_1) == 0 and len(contours_2) == 0 ):
        is_detected = False
    else:
        is_detected = True
    
    state_coor = ((red_coor[0] + yellow_coor[0])//2, (red_coor[1] + yellow_coor[1])//2)
    
    return state_coor, is_detected
