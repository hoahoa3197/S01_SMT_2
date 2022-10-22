import cv2
import numpy as np
import matplotlib.pyplot as plt
def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("Threshhold1","Trackbar",100,255, nothing)
cv2.createTrackbar("Threshhold2","Trackbar",0,255, nothing)
cv2.createTrackbar("Area","Trackbar",10,50000, nothing)

cv2.createTrackbar("minval","Trackbar",90,2048,nothing)
cv2.createTrackbar("maxval","Trackbar",80,2048,nothing)
cv2.createTrackbar("Width","Trackbar",0,255,nothing)
cv2.createTrackbar("Height","Trackbar",0,255,nothing)
cv2.resizeWindow("Trackbar",300,300)



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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray_br = cv2.medianBlur(gray, 7)
    
    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_br,
                    cv2.HOUGH_GRADIENT, 1, 100, param1 = 100,
                param2 = 28, minRadius = 80, maxRadius = 90)

    # Draw circles that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            print(r)

            # Draw the circumference of the circle.
            # cv2.circle(img, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            # cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
    img_resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Detected Circle", img_resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()