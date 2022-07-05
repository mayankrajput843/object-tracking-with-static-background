import cv2
import numpy as np
from matplotlib import pylab as plt
video = cv2.VideoCapture('v2.mp4');
if video.isOpened():
    while True:
        check,frame = video.read();
        _,f2 = video.read()
        if check:
            diff = cv2.absdiff(frame,f2)
            img = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            re, gry = cv2.threshold(img, 127, 227, 00)
            con,_ = cv2.findContours(gry,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(frame,con,-1,(0,255,0),3)
            for i in con:
                (x,y,w,h) = cv2.boundingRect(i)
                if cv2.contourArea(i)<1000 or cv2.contourArea(i)>10000:
                    continue
                else:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow("w1",frame)
            frame = f2
            _,f2 = video.read();
            key = cv2.waitKey(50)
            print(con)
            if key==ord('q'):
                break
        else:
            print("Not open")