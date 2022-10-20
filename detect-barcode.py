# import the necessary packages
import numpy as np
import imutils
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,2048)
cap.set(4,2048)
dataCode = []
while True:
            ret, cv_img = cap.read()
            if ret:
                gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
                # compute the Scharr gradient magnitude representation of the images
                # in both the x and y direction using OpenCV 2.4
                ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
                gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
                gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)
                # subtract the y-gradient from the x-gradient
                gradient = cv2.subtract(gradX, gradY)
                gradient = cv2.convertScaleAbs(gradient)
                # blur and threshold the image
                blurred = cv2.blur(gradient, (9, 9))
                (_, thresh) = cv2.threshold(blurred, 170, 255, cv2.THRESH_BINARY)
                # construct a closing kernel and apply it to the thresholded image
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
                closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
                
                # # find the contours in the thresholded image, then sort the contours
                # # by their area, keeping only the largest one
                cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                print(c)
                # # compute the rotated bounding box of the largest contour
                rect = cv2.minAreaRect(c)
                print(rect)
                box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
                box = np.int0(box)
                # # draw a bounding box arounded the detected barcode and display the
                # # image
                # cv2.drawContours(cv_img, [box], -1, (0, 255, 0), 3)
                
                cv2.imshow("Image", closed)


          
            
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break   