from tkinter import *
import numpy as np
from matplotlib import pylab as plt
import cv2
def p():
    path = PathValue.get()
    min = int(contours_min_val_Entry.get()) #min
    max = int(contours_max_val_Entry.get()) #max
    print(type(path))
    print(type(min))
    print(type(max))
    video = None
    if path=='0':
        video = cv2.VideoCapture(0)
    else:
        video = cv2.VideoCapture(path)
    _, f1 = video.read()
    _, f2 = video.read()
    while video.isOpened():
        diff = cv2.absdiff(f1, f2)
        gry = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gry, (5, 5), 0)
        _, thr = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dil = cv2.dilate(thr, None, iterations=3)
        con, _ = cv2.findContours(dil, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in con:
            (x, y, w, h) = cv2.boundingRect(i)
            #for v2.mp4 => (min:= 700,max:= 15000)
            if cv2.contourArea(i) < min or cv2.contourArea(i) > max:
                continue
            else:
                cv2.rectangle(f1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("img", f1)
        f1 = f2
        _, f2 = video.read()
        key = cv2.waitKey(60)
        if key == ord('q'):
            break
root = Tk()
root.geometry("655x333")
Path = Label(root,text = "Path")
max_val = Label(root,text = "Contours Max Values")
min_val = Label(root,text = "Contours Min Values")
Path.grid(row = 0,column = 0)
max_val.grid(row = 2,column = 0)
min_val.grid(row = 4,column = 0)
# initialize values
PathValue = StringVar()
contours_min_val = IntVar()
contours_max_val = IntVar()
# initialize Entris
PathEntry = Entry(root,textvariable = PathValue)
contours_min_val_Entry = Entry(root,textvariable = contours_min_val)
contours_max_val_Entry = Entry(root,textvariable = contours_max_val)
PathEntry.grid(row=0,column=1)
contours_max_val_Entry.grid(row = 2,column = 1)
contours_min_val_Entry.grid(row = 4,column = 1)
Button(text = "Submit",command = p).grid(row = 6,column = 1)
root.mainloop()