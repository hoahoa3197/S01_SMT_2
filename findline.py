import cv2
import numpy as np

sizeofscr = 500

blank_image = np.zeros((sizeofscr,sizeofscr,3), np.uint8)

p1 = (290,230)
p2 = (100,100)

blank_image = cv2.circle(blank_image, p1, 10, (255, 0, 0), 2)
blank_image = cv2.circle(blank_image, p2, 10, (255, 0, 0), 2)

fx = abs(p1[0] - p2[0])
fy = abs(p1[1] - p2[1])

if (p1[0]+p1[1]) > (p2[0]+p2[1]):
    if fx < fy:
        temp = abs(sizeofscr - p1[1]) / fy

        fx = (temp * fx) + p1[0]
        fy = (temp * fy) + p1[1]

        blank_image = cv2.line(blank_image,(int(fx),int(fy)),p2,(0,0,255),3)

    else:
        temp = abs(sizeofscr - p1[0]) / fx
    
        fx = (temp * fx) + p1[0]
        fy = (temp * fy) + p1[1]
    
        blank_image = cv2.line(blank_image,(int(fx),int(fy)),p2,(0,0,255),3)    
else:
    if fx < fy:
        temp = abs(sizeofscr - p1[1]) / fy

        fx = (temp * fx) + p1[0]
        fy = (temp * fy) + p1[1]

        blank_image = cv2.line(blank_image,(int(fx),int(fy)),p1,(0,0,255),3)
    else:
        temp = abs(sizeofscr - p1[0]) / fx
    
        fx = (temp * fx) + p1[0]
        fy = (temp * fy) + p1[1]
    
    
        blank_image = cv2.line(blank_image,(int(fx),int(fy)),p1,(0,0,255),3)    

cv2.imshow("test",blank_image)
cv2.waitKey(0)