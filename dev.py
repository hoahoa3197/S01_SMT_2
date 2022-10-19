#%%
import cv2
from cv2 import VideoCapture
from cv2 import resize
from cv2 import threshold
import numpy as np
import zxingcpp
import imutils
from pyzbar.pyzbar import decode,ZBarSymbol
def preprocess(image):

	#resize image
	image = cv2.resize(image,None,fx=0.7, fy=0.7, interpolation = cv2.INTER_CUBIC)

	#convert to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	#calculate x & y gradient
	gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
	gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)

	# subtract the y-gradient from the x-gradient
	gradient = cv2.subtract(gradX, gradY)
	gradient = cv2.convertScaleAbs(gradient)

	# blur the image
	blurred = cv2.blur(gradient, (3, 3))

	# threshold the image
	(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
	thresh = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	return thresh
cap = VideoCapture(0)
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
               (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
               
               # construct a closing kernel and apply it to the thresholded image
               kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (31, 7))
               closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
               
               # perform a series of erosions and dilations
               closed = cv2.erode(closed, None, iterations = 4)
               closed = cv2.dilate(closed, None, iterations = 4)
               # find the contours in the thresholded image, then sort the contours
# by their area, keeping only the largest one
               # cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
               #    cv2.CHAIN_APPROX_SIMPLE)
               # cnts = imutils.grab_contours(cnts)
               # c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
               # # compute the rotated bounding box of the largest contour
               # rect = cv2.minAreaRect(c)
               # box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
               # box = np.int0(box)
               # # draw a bounding box arounded the detected barcode and display the
               # # image
               # cv2.drawContours(cv_img, [box], -1, (0, 255, 0), 3)
               cv2.imshow("Image", cv_img)
               cv2.imshow("Closed ", closed)


          
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
               break   
            
# %%
# import cv2
# from dbr import *
# from cv2 import VideoCapture
# license_key = "t0075oQAAAGINs0ZBWeoND009wNJX5ZpaA7h2nkmRGtPXOt+Fb0BvhTpvtjaDx8usaPlG3k5yRQ6Kio9/a6bcav2TiNS+QqIK2QX6LiLL"
# BarcodeReader.init_license(license_key)
# reader = BarcodeReader()
# cap = VideoCapture(0)
# cap.set(3,2048)
# cap.set(4,2048)
# dataCode = []
# ret, cv_img = cap.read()
# if ret:
#    resize_frame = cv2.resize(cv_img,(500,500),interpolation = cv2.INTER_CUBIC)
#    try:
#       text_results = reader.decode_file(r'C:\Users\BOSS\Desktop\VT2\185.bmp')

#       if text_results != None:
#          for text_result in text_results:
#                print("Barcode Format : ")
#                print(text_result.barcode_format_string)
#                print("Barcode Text : ")
#                print(text_result.barcode_text)
#                print("Localization Points : ")
#                print(text_result.localization_result.localization_points)
#                print("Exception : ")
#                print(text_result.exception)
#                print("-------------")
#    except BarcodeReaderError as bre:
#       print(bre)
# cv2.imshow("Frame", resize_frame)
# cv2.waitKey(0)
