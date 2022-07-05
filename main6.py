import cv2
track = cv2.TrackerKCF_create()
video = cv2.VideoCapture("v3(360).mp4")
while True:
    k,frame = video.read()
    cv2.imshow("Tracking",frame)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
bbox = cv2.selectROI("Tracking",frame,False)
ok = track.init(frame,bbox)
while True:
    ok,frame = video.read()
    ok,bbox = track.update(frame)
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]),
              int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 0, 255), 2, 2)

    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(25) & 0xff
    if k == 27:break
