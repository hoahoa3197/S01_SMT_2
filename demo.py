from calendar import c
import math
import cv2
from matplotlib.path import Path
import numpy as np
import matplotlib.pyplot as plt
import os 
import zxingcpp
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
cv2.createTrackbar("Threshhold1","Trackbar",170,255, nothing)
cv2.createTrackbar("Threshhold2","Trackbar",0,255, nothing)
cv2.createTrackbar("Area","Trackbar",10000,50000, nothing)

cv2.createTrackbar("minval","Trackbar",0,10000,nothing)
cv2.createTrackbar("maxval","Trackbar",0,50000,nothing)
cv2.createTrackbar("Width","Trackbar",0,255,nothing)
cv2.createTrackbar("Height","Trackbar",0,255,nothing)

cap = cv2.VideoCapture(0)
cap.set(3,2048)
cap.set(4,2048)

while True:
    _,img = cap.read()
    thresh1 = cv2.getTrackbarPos("Threshhold1","Trackbar")
    thresh2 = cv2.getTrackbarPos("Threshhold2","Trackbar")
    value_area = cv2.getTrackbarPos("Area","Trackbar")
    min_val = cv2.getTrackbarPos("minval","Trackbar")
    max_val = cv2.getTrackbarPos("maxval","Trackbar")
    val_width = cv2.getTrackbarPos("Width","Trackbar")
    val_heigt = cv2.getTrackbarPos("Height","Trackbar")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_resize = cv2.resize(gray,(500,500),interpolation=cv2.INTER_CUBIC)
    ret,thresh_tem = cv2.threshold(gray.copy(),thresh1  ,255,cv2.THRESH_BINARY)
    kernel = np.ones((1,1), np.uint8)
    thresh_tem = cv2.erode(thresh_tem, kernel, cv2.BORDER_REFLECT)
    contours, hierarchy = cv2.findContours(thresh_tem,
        cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    
    dataResult = zxingcpp.read_barcodes(img)
    if dataResult is not None:
        for data in dataResult:
            if str(data.format) == "BarcodeFormat.DataMatrix" or str(data.format) == "BarcodeFormat.QRCode":
                [x1,y1] = data.position.bottom_left.x,data.position.bottom_left.y
                [x2,y2] = data.position.bottom_right.x,data.position.bottom_right.y
                [x3,y3] = data.position.top_right.x,data.position.top_right.y
                [x4,y4] = data.position.top_left.x,data.position.top_left.y
                pts = np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,(0,255,255),10)
                # TIM TEM
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    print(area)
                    if area >40000:
                        resultPoint1 = cv2.pointPolygonTest(cnt, (x1,y1), False) 
                        resultPoint2 = cv2.pointPolygonTest(cnt, (x2,y2), False)
                        resultPoint3 = cv2.pointPolygonTest(cnt, (x3,y3), False)
                        resultPoint4 = cv2.pointPolygonTest(cnt, (x4,y4), False)
                        if int(resultPoint1) == 1 and int(resultPoint2) == 1 and int(resultPoint3) == 1 and int(resultPoint4) == 1:
                            x, y, w, h = cv2.boundingRect(cnt)
                            rect = cv2.minAreaRect(cnt)
                            box = cv2.boxPoints(rect)
                            box = np.int0(box)
                            M = cv2.moments(box)
                            cX = int(M["m10"] / M["m00"])
                            cY = int(M["m01"] / M["m00"])
                            
    # draw the contour and center of the shape on the image
                            cv2.drawContours(img,[box],-1, (0, 255, 0),5)
                            cv2.circle(img, (cX, cY), 1, (255, 255, 255), -1)
                            cv2.putText(img, "center", (cX - 20, cY - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
            
    anh1 = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
    cv2.imshow("FRAME", anh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release 
# Destroy all the windows
cv2.destroyAllWindows()
                
                
      
