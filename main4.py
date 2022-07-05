import cv2
import numpy as np
from matplotlib import pylab as plt
video = cv2.VideoCapture(0)
if video.isOpened():
    while True:
        check,frame = video.read()
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if check:
            re,gry = cv2.threshold(img,127,255,0)
            cv2.imshow('img1',gry)
            con,_ = cv2.findContours(gry,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(frame,con,-1,(0,255,0),3)
            cv2.imshow("i1",frame)
            key = cv2.waitKey(50)
            if key==ord('q'):
                break
        else:
            print("not open")
