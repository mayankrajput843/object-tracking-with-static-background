import cv2
from matplotlib import pylab as py
video = cv2.VideoCapture('v2.mp4')
_,f1 = video.read()
_,f2 = video.read()
while video.isOpened():
    diff = cv2.absdiff(f1,f2)
    gry = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gry,(5,5),0)
    _, thr = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dil = cv2.dilate(thr,None,iterations=3)
    con,_ = cv2.findContours(dil,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i in con:
        (x,y,w,h) = cv2.boundingRect(i)
        if cv2.contourArea(i)<700 or cv2.contourArea(i)>15000:
            continue
        else:
            cv2.rectangle(f1,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("img",f1)
    f1 = f2
    _,f2 = video.read()
    key = cv2.waitKey(20)
    if key == ord('q'):
        break
    cv2.destroyAllWindows()



