import cv2
import numpy as np
import matplotlib.pyplot as plt
def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("Threshhold1","Trackbar",100,255, nothing)
cv2.createTrackbar("Threshhold2","Trackbar",0,255, nothing)
cv2.createTrackbar("Area","Trackbar",10,50000, nothing)

cv2.createTrackbar("Width","Trackbar",0,255,nothing)
cv2.createTrackbar("Height","Trackbar",0,255,nothing)

cap = cv2.VideoCapture(0)
cap.set(3,2048)
cap.set(4,2048)

while True:
    thresh1 = cv2.getTrackbarPos("Threshhold1","Trackbar")
    thresh2 = cv2.getTrackbarPos("Threshhold2","Trackbar")
    value_area = cv2.getTrackbarPos("Area","Trackbar")
    width = cv2.getTrackbarPos("Width","Trackbar")
    height = cv2.getTrackbarPos("Height","Trackbar")

    # Let's load a simple image with 3 black squares
    _,img = cap.read()
    img_resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_resize = cv2.resize(gray,(500,500),interpolation=cv2.INTER_CUBIC)
    ret,thresh_img = cv2.threshold(gray_resize,thresh1,255,cv2.THRESH_BINARY)
    kernel = np.ones((2,2), np.uint8)
    
    # Using cv2.erode() method 
    thresh_img = cv2.erode(thresh_img, kernel, cv2.BORDER_REFLECT)

    contours, hierarchy = cv2.findContours(thresh_img,
        cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >value_area:
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
            
            
           
    cv2.imshow('Canny Edges After Contouring', thresh_img)
    cv2.imshow('Contours', img_resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()