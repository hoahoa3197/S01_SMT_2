from tkinter import N
import cv2
import numpy as np
import zxingcpp
import math

def get_distance(start_point, dest_point):
    x1, y1 = start_point
    x2, y2 = dest_point
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist
def linePoints(x0,  y0,  x1,  y1):
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
        print("End_point:" ,end_points)
        Points=linePoints(start_point[0],start_point[1],end_points[0],end_points[1])
        
        for point in Points:
            if abs(get_distance(dest_point,point)-get_distance(start_point,dest_point))<=0.5:
                if point!=start_point:
                    res_point=point
        return res_point
def read_barcode_zxing(frame):
        resultScanCode = zxingcpp.read_barcodes(frame)
        if resultScanCode != []:
            for result in resultScanCode:
                if str(result.format) == "BarcodeFormat.DataMatrix" or str(result.format) == "BarcodeFormat.QRCode":
                    [x1,y1] = result.position.bottom_left.x,result.position.bottom_left.y
                    [x2,y2] = result.position.bottom_right.x,result.position.bottom_right.y
                    [x3,y3] = result.position.top_right.x,result.position.top_right.y
                    [x4,y4] = result.position.top_left.x,result.position.top_left.y
                    return {'data' :result.text.split(","),'pos1': [x1,y1],'pos2': [x2,y2],'pos3': [x3,y3],'pos4': [x4,y4]}
        else :
            return None
def findOppositePoint(image,val_thresh,areaTem = 1000):
    """
    Find stamp position, Centroid Axis and return opposite point paste stamp print
        Return : - Data QR of tem
                 - Opposite point (x,y)
    """
    #Stamp Process
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,thresh_tem = cv2.threshold(gray.copy(),val_thresh,255,cv2.THRESH_BINARY)
    kernel = np.ones((1,1), np.uint8)
    thresh_tem = cv2.erode(thresh_tem, kernel, cv2.BORDER_REFLECT)
    contours, _ = cv2.findContours(thresh_tem,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #Axis Process
    blur_img = cv2.medianBlur(gray,171)
    thresh_meanC = cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(thresh_meanC, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    detected_circles = cv2.HoughCircles(dilation, method=cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=25,minRadius=50, maxRadius=90)
    pointCenterTem=None
    Point_Cirle=None


    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 150000:
            
            x,y,w,h=cv2.boundingRect(cnt)
            tem_ROI=image[y:y+h,x:x+w]
            dataResult = read_barcode_zxing(tem_ROI)
            if dataResult is not None:
                dataCode = dataResult['data'] #Global data
                print(dataCode)
                pos1 = ( dataResult['pos1'][0]+x, dataResult['pos1'][1]+y)
                pos2 = ( dataResult['pos2'][0]+x, dataResult['pos2'][1]+y)
                pos3 = ( dataResult['pos3'][0]+x, dataResult['pos3'][1]+y)
                pos4 = ( dataResult['pos4'][0]+x, dataResult['pos4'][1]+y)
                resultPoint1 = cv2.pointPolygonTest(cnt, pos1, False) 
                resultPoint2 = cv2.pointPolygonTest(cnt, pos2, False)
                resultPoint3 = cv2.pointPolygonTest(cnt, pos3, False)
                resultPoint4 = cv2.pointPolygonTest(cnt, pos4, False)
                print("Result position : ",resultPoint1,resultPoint2,resultPoint3,resultPoint4)
                if int(resultPoint1) == 1 and int(resultPoint2) == 1 and int(resultPoint3) == 1 and int(resultPoint4) == 1:
                    rect = cv2.minAreaRect(cnt)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    M = cv2.moments(box)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    print("Finded Centroid Stamp : ", (cX,cY))
                    pointCenterTem = (cX,cY)
    # Draw circles that are detected.
    if detected_circles is not None:
        print('The axis centroid has been found !')
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
        print(detected_circles)
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            Point_Cirle = (a, b)
            # Draw the circumference of the circle.
            cv2.circle(image, (a, b), r, (0, 255, 0), 5)
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(image, (a, b), 1, (0, 0, 255), 5)
        if  Point_Cirle is not None and pointCenterTem is not None:
                cv2.drawContours(image,[box],-1, (255, 255, 0),5)
                cv2.circle(image, (cX, cY), 10, (0, 255, 0),10)
                cv2.putText(image, str((cX, cY)), (cX - 30, cY -30),cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 5)
                cv2.line(image,(cX,cY),(a,b),(255,255,0),5)
                end_point = getDesPoint(image,(cX,cY),(a,b))
                cv2.circle(image, end_point, 5, (0, 0, 255), -1)
                cv2.line(image,(a,b),(end_point),(255,255,255),5)
       
    else:
        print("Can't find the axis center !")
    imageOrigin= cv2.resize(image,(500,500))
    threshStamp = cv2.resize(thresh_tem ,(500,500))
    houghCircle = cv2.resize(dilation ,(500,500))
    cv2.imshow('imageOrigin', imageOrigin)
    cv2.imshow('threshStamp',threshStamp)
    cv2.imshow('houghCircle',houghCircle)



def nothing(x):
    pass

cv2.namedWindow("Config")
cv2.createTrackbar("Threshhold1","Config",100,255, nothing)
cv2.createTrackbar("Area","Config",10,50000, nothing)
image = cv2.imread(r'C:\Users\BOSS\Desktop\S01_SMT_2\Data\image\CT4.png')
cap = cv2.VideoCapture(0)
cap.set(3,2048)
cap.set(4,2048)
while True:
    _,img = cap.read()
    result = findOppositePoint(img,160,10000)
    print(result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break