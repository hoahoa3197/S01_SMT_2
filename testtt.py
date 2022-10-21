from calendar import c
import math
import cv2
from matplotlib.path import Path
import numpy as np
import matplotlib.pyplot as plt
import os 
import os
curDir = os.path.dirname(os.path.realpath(__file__))
print(curDir)
img_path = os.path.join(curDir,"image")
print(img_path)
def get_distance(start_point, dest_point):
    x1, y1 = start_point
    x2, y2 = dest_point
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

def linePoints( x0,  y0,  x1,  y1):
    pointsOfLine=[]

    dx = abs(x1-x0)
    sx =  1 if x0<x1 else -1
    dy = abs(y1-y0)
    sy = 1 if y0<y1 else -1
    err = (dx if dx>dy else  -dy)/2

    while 1:

        pointsOfLine.append((x0,y0))
        if x0==x1 and y0==y1:
            break
        e2 = err
        if e2 >-dx:
            err -= dy
            x0 += sx
        if e2 < dy:
            err += dx
            y0 += sy
    return pointsOfLine
def getDesPoint(sizeofscr,start_point,dest_point):
        res_point=None
        fx = abs(start_point[0] - dest_point[0])
        fy = abs(start_point[1] - dest_point[1])
        end_points=None
        if (start_point[0] + start_point[1]) > (dest_point[0] + dest_point[1]):
            if fx < fy:
                temp = abs(sizeofscr - start_point[1]) / fy

                fx = (temp * fx) + start_point[0]
                fy = (temp * fy) + start_point[1]
                end_points= (int(fx), int(fy))
            else:
                temp = abs(sizeofscr - start_point[0]) / fx

                fx = (temp * fx) + start_point[0]
                fy = (temp * fy) + start_point[1]
                end_points = (int(fx), int(fy))
        else:
            if fx < fy:
                temp = abs(sizeofscr - start_point[1]) / fy

                fx = (temp * fx) + start_point[0]
                fy = (temp * fy) + start_point[1]
                end_points = (int(fx), int(fy))
            else:
                temp = abs(sizeofscr - start_point[0]) / fx

                fx = (temp * fx) + start_point[0]
                fy = (temp * fy) + start_point[1]
                end_points = (int(fx), int(fy))
        Points=linePoints(start_point[0],start_point[1],end_points[0],end_points[1])
        # cv2.line(blank_image, start_point, end_points, (255, 0, 0), 2)
        # cv2.circle(blank_image, start_point, 10, (0, 255, 0), -1)
        # cv2.circle(blank_image, dest_point, 10, (0, 255, 255), -1)
        for point in Points:
            if abs(get_distance(dest_point,point)-get_distance(start_point,dest_point))<=0.5:
                if point!=start_point:
                    res_point=point
        return res_point
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

path=r'C:\Users\BOSS\Desktop\B01-SMT\Data\image\\'
files =os.listdir(path)
img = cv2.imread(r'C:\Users\BOSS\Desktop\B01-SMT\Data\image\28972.png')

for file in files:
    img=cv2.imread(path+file)
    thresh1 = cv2.getTrackbarPos("Threshhold1","Trackbar")
    thresh2 = cv2.getTrackbarPos("Threshhold2","Trackbar")
    value_area = cv2.getTrackbarPos("Area","Trackbar")
    min_val = cv2.getTrackbarPos("minval","Trackbar")
    max_val = cv2.getTrackbarPos("maxval","Trackbar")
    val_width = cv2.getTrackbarPos("Width","Trackbar")
    val_heigt = cv2.getTrackbarPos("Height","Trackbar")
    img_resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_resize = cv2.resize(gray,(500,500),interpolation=cv2.INTER_CUBIC)
    ret,thresh_tem = cv2.threshold(gray_resize.copy(),163,255,cv2.THRESH_BINARY)
    
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
    
    edge = cv2.Canny(gray_resize,97,97)
    
    kernel = np.ones((1,1), np.uint8)
    thresh_tem = cv2.erode(edge, kernel, cv2.BORDER_REFLECT)
    
    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(thresh_tem,
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                param2 = 30, minRadius = 20, maxRadius = 35)

    # Draw circles that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integerss.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            r = int(math.sqrt((a-cX)**2 +(b-cY)**2))
            circel_big = cv2.circle(img_resize, (a, b), r, 180, 2)
            
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img_resize, (a, b), 1, (0, 0, 255), 3)
            cv2.line(img_resize,(cX,cY),(a,b),(255,255,0))

            end_point = getDesPoint(500,(cX,cY),(a,b))
        

        cv2.line(img_resize,(a,b),(end_point),(255,255,255))
    
            
    cv2.imshow('Thresh tem', thresh_tem)
    cv2.imshow('Contours', img_resize)
    cv2.waitKey(0)
    
    
    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #     break
# After the loop release 
# Destroy all the windows
cv2.destroyAllWindows()