 #Get position paste
from tkinter.messagebox import NO
import cv2
from cv2 import VideoCapture
import numpy as np
import matplotlib.pyplot as plt
import math
import zxingcpp
def nothing(x):
    pass

cv2.namedWindow("1")
cv2.createTrackbar("Threshhold1","1",100,255, nothing)
cv2.createTrackbar("Threshhold2","1",0,255, nothing)
cv2.createTrackbar("minval","1",90,2048,nothing)
cv2.createTrackbar("maxval","1",80,2048,nothing)
cv2.createTrackbar("Width","1",0,255,nothing)
cv2.createTrackbar("Height","1",0,255,nothing)


def read_barcode_zxing( frame):
        resultScanCode = zxingcpp.read_barcodes(frame)
        for result in resultScanCode:
            if str(result.format) == "BarcodeFormat.DataMatrix" or str(result.format) == "BarcodeFormat.QRCode":
                [x1,y1] = result.position.bottom_left.x,result.position.bottom_left.y
                [x2,y2] = result.position.bottom_right.x,result.position.bottom_right.y
                [x3,y3] = result.position.top_right.x,result.position.top_right.y
                [x4,y4] = result.position.top_left.x,result.position.top_left.y
                pointQR = np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
                # pointQR = pointQR.reshape((-1,1,2))
                return {'data' :result.text.split(","),'pos1': [x1,y1],'pos2': [x2,y2],'pos3': [x3,y3],'pos4': [x4,y4]}
            # DataMaxtrix format : PN_Vendor_LOT_DateCode_Quantity_MaCongDon_CreateDate(timestamp)
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

def getDesPoint(image,start_point,dest_point):
    hei,wid,_=image.shape
    res_point=None
    fx = abs(start_point[0] - dest_point[0])
    fy = abs(start_point[1] - dest_point[1])
    end_points=None
    theta = np.arctan2(start_point[1]-dest_point[1], start_point[0]-dest_point[0])
    endpt_x = int(start_point[0] - 2500*np.cos(theta))
    endpt_y = int(start_point[1] - 2500*np.sin(theta))
    end_points= (endpt_x, endpt_y)
    # print("End_point:" ,end_points)
    Points=linePoints(start_point[0],start_point[1],end_points[0],end_points[1])
    # print(get_distance(start_point,dest_point))
    # cv2.line(image,start_point,end_points,  (0, 255, 255), 5)
    # cv2.imshow('fff',image)
    for point in Points:
        if abs(get_distance(dest_point,point)-get_distance(start_point,dest_point))<=0.5:
            if point!=start_point:
                res_point=point
    return res_point
# cap = cv2.imread(r'C:\Users\BOSS\Desktop\B01-SMT\Data\image\CT4.png')
cap = VideoCapture(0)
cap.set(3,2048)
cap.set(4,2048)

while True:
    _,cv_img = cap.read()
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    ret,thresh_tem = cv2.threshold(gray.copy(),210,255,cv2.THRESH_BINARY)
    kernel = np.ones((1,1), np.uint8)
    thresh_tem = cv2.erode(thresh_tem, kernel, cv2.BORDER_REFLECT)
    contours, hierarchy = cv2.findContours(thresh_tem,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    pointCenterTem=None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >250000:
            x,y,wid,hei=cv2.boundingRect(cnt)
            img_read=cv_img[y:y+hei,x:x+wid]
            dataResult = read_barcode_zxing(img_read)
            if dataResult is not None:
                pos1 =(dataResult['pos1'][0]+x,dataResult['pos1'][1]+y)
                pos2 =(dataResult['pos2'][0]+x,dataResult['pos2'][1]+y)
                pos3 =(dataResult['pos3'][0]+x,dataResult['pos3'][1]+y)
                pos4 =(dataResult['pos4'][0]+x,dataResult['pos4'][1]+y)
                resultPoint1 = cv2.pointPolygonTest(cnt, pos1, False) 
                resultPoint2 = cv2.pointPolygonTest(cnt, pos2, False)
                resultPoint3 = cv2.pointPolygonTest(cnt, pos3, False)
                resultPoint4 = cv2.pointPolygonTest(cnt, pos4, False)
                if int(resultPoint1) == 1 and int(resultPoint2) == 1 and int(resultPoint3) == 1 and int(resultPoint4) == 1:
                    rect = cv2.minAreaRect(cnt)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    M = cv2.moments(box)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    pointCenterTem =(cX,cY)
        #             # draw the contour and center of the shape on the image
                    cv2.drawContours(cv_img,[box],-1, (255, 255, 0),5)
                    cv2.circle(cv_img, (cX, cY), 1, (255, 255, 255),5)
                    cv2.putText(cv_img, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 5)
    blur_img = cv2.medianBlur(gray,111)
    thresh_meanC = cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(thresh_meanC, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    detected_circles = cv2.HoughCircles(dilation, method=cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=20,minRadius=60, maxRadius=75)
    Point_Cirle=None
    # Draw circles that are detected.
    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            print(r)
            Point_Cirle=(a, b)
            # Draw the circumference of the circle.
            cv2.circle(cv_img, (a, b), r, (0, 255, 0), 5)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(cv_img, (a, b), 1, (0, 0, 255), 5)
            
    if  Point_Cirle is not None and pointCenterTem is not None:
            cv2.line(cv_img,(cX,cY),(a,b),(255,255,0),5)
            hei,wid,_=cv_img.shape
            end_point = getDesPoint(cv_img,(cX,cY),(a,b))
            cv2.circle(cv_img, end_point, 5, (0, 0, 255), -1)
            cv2.line(cv_img,(a,b),(end_point),(255,255,255),5)
            print(end_point)
    anh1= cv2.resize(cv_img,(500,500))
    thresh_resize = cv2.resize(thresh_tem   ,(500,500))
    cv2.imshow('Contours', anh1)
    cv2.imshow('thresh_resize',thresh_resize)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        