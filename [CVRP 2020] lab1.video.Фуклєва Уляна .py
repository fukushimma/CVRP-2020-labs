import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()

cap2=cv2.VideoCapture('output.avi') 
while(cap2.isOpened()):
    ret2, frame2 = cap2.read()
    if ret2==True:
        gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY) 
        gray1 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) 
        gray2 = cv2.rectangle(gray1, (60, 20), (400, 200),  (0,0,255), 5)
        gray3 = cv2.line(gray2, (60, 20), (400, 200),(255,0,255) , 5)  
        cv2.imshow('frame2',gray3)  
        
    else:
        break    
    if cv2.waitKey(100) & 0xFF == ord('z'):
            break   
   
out.release()
cv2.destroyAllWindows()
