import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def motionCapture(file , **kwarg):
    capture = cv2.VideoCapture(file)
    object_detector = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold=50)

    _, fr = capture.read()
    height , width , _ = fr.shape

    x_pos = []
    y_pos = []

    while True:

        ret, frame = capture.read()

        mask = object_detector.apply(frame)
        _ , mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100 and area < 300:
                #cv2.drawContours(frame,[cnt],-1,(0,0,255),5)
                x , y , w , h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 5)
                x_pos.append(x+w/2)
                y_pos.append(y+h/2)

        if kwarg["show_track"]:
            cv2.imshow("Frame", frame)
        if kwarg["show_mask"]:
            cv2.imshow("Mask", mask)
        
        key = cv2.waitKey(30)
        if key == 27:
            break

    return x_pos , y_pos 

def curvature(x_pos , y_pos , dt):
    n = len(x_pos)-1

    x = np.array(x_pos)
    y = np.array(y_pos)

    fx = np.roll(x,1)
    bx = np.roll(x,-1)
    fy = np.roll(y,1)
    by = np.roll(y,-1)

    dx = (fx-bx)/(2*dt)
    dy = (fy - by)/(2*dt)

    ddx = (fx+bx-2*x)/(dt**2)
    ddy = (fy+by-2*y)/(dt**2)

    k = (dx*ddy-dy*ddx)/np.power(np.power(dx,2)+np.power(dy,2),3/2)
    return k[1:-1]

x , y = motionCapture("kiloBot5T1.mp4", show_track = True , show_mask = True)

print(x,"\n\n\n",y)
