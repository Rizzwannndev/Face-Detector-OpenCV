import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
vidCapt = cv2.VideoCapture(0)

while True:
    # Where ret refers to rectangle and frame refers to the image.
    ret,frame = vidCapt.read()
    colTrans = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f = faceCascade.detectMultiScale(colTrans, 1.3, 6)

    for (x1, y1, w1, h1) in f:
        cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (88, 255, 50), 5)

    cv2.imshow("WebCam", frame)
    waitTime = cv2.waitKey(40) & 0xff
    if waitTime == 40:
        break

vidCapt.release()
cv2.destroyAllWindows()
