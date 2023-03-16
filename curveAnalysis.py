import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def motionCapture(file , fps, **kwarg):
    capture = cv2.VideoCapture(file)
    object_detector = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold=100)

    _, fr = capture.read()
    height , width , _ = fr.shape

    x_pos = []
    y_pos = []
    t = []

    iter = 0
    while True:
        iter += 1
        t.append(iter/fps)

        ret, frame = capture.read()

        mask = object_detector.apply(frame)
        contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1500:
                #cv2.drawContours(frame,[cnt],-1,(0,0,255),5)
                x , y , w , h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 5)
                if iter%2 == 1:
                    x_pos.append(x+w/2)
                    y_pos.append(y+w/2)
                    t.append(iter/15)

        if kwarg["show_track"]:
            cv2.imshow("Frame", frame)
        
        key = cv2.waitKey(30)
        if key == 27:
            break

    return x_pos , y_pos , t

def curvature(x_pos , y_pos , t):
    x = np.array(x_pos)
    y = np.array(y_pos)
    t = np.delete(np.array(t),0)

    px1 = np.delete(np.roll(x,1),0)
    x1 = np.delete(x,0)
    py1 = np.delete(np.roll(y,1),0)
    y1 = np.delete(y,0)

    dx = (px1 - x1)/t
    dy = (py1 - y1)/t

    px2 = np.delete(np.roll(dx,1),0)
    x2 = np.delete(dx,0)
    py2 = np.delete(np.roll(dy,1),0)
    y2 = np.delete(dy,0)

    t2 = np.delete(t,0)

    ddx = (px2 - x2)/t2
    ddy = (py2 - y2)/t2

    dx = np.delete(dx,0)
    dy = np.delete(dy,0)

    return (dx*ddy-dy*ddx)/np.power(np.power(dx,2)+np.power(dy,2),3/2)


