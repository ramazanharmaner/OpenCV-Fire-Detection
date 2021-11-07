import cv2

vid=cv2.VideoCapture("yangin.mp4")
yangin_cascade=cv2.CascadeClassifier("yangin_cascade\\yangin_cascade.xml")

while True:
    ret,frame=vid.read()
    frame=cv2.resize(frame,(480,360))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yangin=yangin_cascade.detectMultiScale(gray,7,10)

    for(x,y,w,h) in yangin:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Yangin Tespiti",frame)

    if cv2.waitKey(20)&0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()