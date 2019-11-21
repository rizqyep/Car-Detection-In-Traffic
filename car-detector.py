import cv2

detect='cars.xml'
vid='video2.avi' #change this into your video path file
cap=cv2.VideoCapture(vid)
car_detect=cv2.CascadeClassifier(detect)

while True :
    ret,img=cap.read() 
    if(type(img)==type(None)): # 
        break
    grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert the frame into grayscale format
    cars = car_detect.detectMultiScale(gscale,scaleFactor=1.1,minNeighbors=1) #adjust value int the scaleFactor and minNeighbors to improve accuracy

    for(x,y,w,h) in cars:
        cv2.rectangle(gbr,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('video',img)
    if cv2.waitKey(33)==27:
        break

cv2.destroyAllWindows()
