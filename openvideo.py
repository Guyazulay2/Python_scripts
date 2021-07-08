import cv2
import numpy as np
import mediapipe
import random
from time import sleep

cap = cv2.VideoCapture(0)
print("Video Open !" if cap else 'not')
if (cap.isOpened()== False):
    print("Error opening video !")

fource = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fource,24.0,(640,480))
font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.putText(frame, 
                'Video 0', 
                (60, 60), 
                font, 1, 
                (0, 255, 0), 
                2, 
                cv2.LINE_4)
    if ret == True:
        out.write(frame)
        cv2.imshow('output',frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
