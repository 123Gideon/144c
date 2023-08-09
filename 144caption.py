import cv2
import numpy as np
import time

cap=cv2.VideoCapture(0)
time.sleep(3)

count=0
background=0

for i in range(60):
    returnV,background=cap.read()
background=np.flip(background,axis=1)



while (cap.isOpened()):
    dummy,image=cap.read()
    image=cv2.flip(image,1)

    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lower_red,upper_red)


    lower_red=np.array([170,120,50])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red,upper_red)



    finalMask=mask1+mask2

    finalMask1=cv2.morphologyEx(finalMask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))

    finalMask2=cv2.bitwise_not(finalMask1)

    result1=cv2.bitwise_and(image,image,mask=finalMask2)
    result2=cv2.bitwise_and(background,background,mask=finalMask1)


    finalOutput=cv2.addWeighted(result1,1,result2,1,0)


    # cv2.imshow("window",image)
    # cv2.imshow("hsv",hsv)
    # cv2.imshow("mask1",mask1)
    # cv2.imshow("mask2",mask2)
    # cv2.imshow("finalMask",finalMask)

    cv2.imshow("r2",result2)
    cv2.imshow("final",finalOutput)
    if cv2.waitKey(25)==32:
        break
    

    

cap.release()
cv2.destroyAllWindows()