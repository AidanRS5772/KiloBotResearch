import cv2
import numpy
import matplotlib.pyplot as plt

capture = cv2.VideoCapture("motionTrackExample.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history = 100, varThreshold=100)

_, fr = capture.read()
height , width , _ = fr.shape

x_pos = []
y_pos = []
t = []

iter = 0
while True:
    iter += 1
    t.append(iter/30)

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

    #cv2.imshow("Mask",mask)
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()

y_pos.reverse()
plt.scatter(x_pos,y_pos)
plt.show()

