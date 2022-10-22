
import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow("1")
cv2.createTrackbar("Threshhold1","1",170,255, nothing)
cv2.createTrackbar("Threshhold2","1",0,255, nothing)
cv2.createTrackbar("Area","1",10000,50000, nothing)

cv2.createTrackbar("minval","1",0,10000,nothing)
cv2.createTrackbar("maxval","1",0,50000,nothing)
cv2.createTrackbar("Width","1",0,255,nothing)
cv2.createTrackbar("Height","1",0,255,nothing)

cap = cv2.VideoCapture(0)
cap.set(3,2048)
cap.set(4,2048)
while True:
    thresh1 = cv2.getTrackbarPos("Threshhold1","1")
    thresh2 = cv2.getTrackbarPos("Threshhold2","1")
    value_area = cv2.getTrackbarPos("Area","1")
    min_val = cv2.getTrackbarPos("minval","1")
    max_val = cv2.getTrackbarPos("maxval","1")
    val_width = cv2.getTrackbarPos("Width","1")
    val_heigt = cv2.getTrackbarPos("Height","1")
    _,img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur_img = cv2.medianBlur(img,121)
    thresh_meanC = cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(thresh_meanC, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    circles = cv2.HoughCircles(dilation, method=cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=25,
                               minRadius=60, maxRadius=90)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        blue = (0, 0, 255)
        green = (0, 255, 0)
        for i in circles[0, :]:
            # draw the outer circle
            print(i[2])
            cv2.circle(img,(i[0],i[1]),i[2], green, 2)
            
            # draw the center of the circle
            cv2.circle(img, (i[0], i[1]), 2, blue, 3)
    
    
    img_resize  = cv2.resize(img,(500,500))
    thresh_resize = cv2.resize(thresh_meanC,(500,500))
    imgray_resize = cv2.resize(dilation,(500,500))
    
    cv2.imshow("orgiin",img_resize)
    cv2.imshow("thr1esh",thresh_resize)
    cv2.imshow("candy",imgray_resize)
    
    
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cv2.destroyAllWindows()