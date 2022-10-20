import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
curDir = os.path.dirname(os.path.realpath(__file__))
print(curDir)
img_path = os.path.join(curDir,"image")
print(img_path)
def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("Threshhold1","Trackbar",100,255, nothing)
cv2.createTrackbar("Threshhold2","Trackbar",0,255, nothing)
cv2.createTrackbar("Area","Trackbar",10,50000, nothing)

cv2.createTrackbar("minval","Trackbar",0,10000,nothing)
cv2.createTrackbar("maxval","Trackbar",0,50000,nothing)
cv2.createTrackbar("Width","Trackbar",0,255,nothing)
cv2.createTrackbar("Height","Trackbar",0,255,nothing)



cap = cv2.VideoCapture(0)
cap.set(3,2048)
cap.set(4,2048)

while True:
    thresh1 = cv2.getTrackbarPos("Threshhold1","Trackbar")
    thresh2 = cv2.getTrackbarPos("Threshhold2","Trackbar")
    value_area = cv2.getTrackbarPos("Area","Trackbar")
    min_val = cv2.getTrackbarPos("minval","Trackbar")
    max_val = cv2.getTrackbarPos("maxval","Trackbar")
    val_width = cv2.getTrackbarPos("Width","Trackbar")
    val_heigt = cv2.getTrackbarPos("Height","Trackbar")

    # Let's load a simple image with 3 black squares
    _,img = cap.read()
    img_resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_resize = cv2.resize(gray,(500,500),interpolation=cv2.INTER_CUBIC)
    ret,thresh_tem = cv2.threshold(gray_resize.copy(),118,255,cv2.THRESH_BINARY)
    
    kernel = np.ones((1,1), np.uint8)
    thresh_tem = cv2.erode(thresh_tem, kernel, cv2.BORDER_REFLECT)
    contours, hierarchy = cv2.findContours(thresh_tem,
        cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >10000:
            x, y, w, h = cv2.boundingRect(cnt)
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            M = cv2.moments(box)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            # draw the contour and center of the shape on the image
            cv2.drawContours(img_resize,[box],-1, (0, 255, 0))
            cv2.circle(img_resize, (cX, cY), 1, (255, 255, 255), -1)
            cv2.putText(img_resize, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    #Thresh truc
    
    edge = cv2.Canny(gray_resize,thresh1,thresh2)
    
    kernel = np.ones((1,1), np.uint8)
    thresh_tem = cv2.erode(edge, kernel, cv2.BORDER_REFLECT)
    
    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(thresh_tem,
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                param2 = 22, minRadius = 20, maxRadius = 30)

    # Draw circles that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integerss.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            r = int(math.sqrt((a-cX)**2 +(b-cY)**2))
            circel_big = cv2.circle(img_resize, (a, b), r, 180, 2)
            img_temp = np.zeros((500,500),np.uint8)
            cv2.circle(img_temp,(250,250),100,255)
            points_circle=np.transpose(np.where(img_resize==255))
            for point in points_circle:
                pass
            
            
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img_resize, (a, b), 1, (0, 0, 255), 3)
            cv2.imshow('haha', img_temp)
    cv2.line(img_resize,(cX,cY),(a,b),(255,255,0))
    
            
    cv2.imshow('Thresh tem', thresh_tem)
    cv2.imshow('Contours', img_resize)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()