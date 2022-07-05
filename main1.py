import cv2
def clicl_event(ev,x,y,flag,pr):
    if ev == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
video = cv2.VideoCapture(0)
if video.isOpened():
    while True:
        check, frame = video.read()
        if check:
            gry = frame
            v1 = cv2.resize(gry,(512,512))
            cv2.imshow('Color Frame', v1)
            cv2.setMouseCallback('Color Frame', clicl_event)
            key = cv2.waitKey(50)
            if key == ord('q'):
                break
        else:
            print('Frame not available')
            print(video.isOpened())