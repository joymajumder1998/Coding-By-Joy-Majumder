#Enhancement
import cv2

img=cv2.imread('sal.png')
clahe=cv2.createCLAHE
t=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('save.png',t)
if cv2.waitKey(0) & 0xFF == ord('q'): 
    cv2.destroyAllWindows()