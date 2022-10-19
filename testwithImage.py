import cv2
from cv2 import imread
import numpy as np
import matplotlib.pyplot as plt
img = imread(r'C:\Users\BOSS\Desktop\B01-SMT\Data\image\IMG_20221019_140511.jpg')

img_resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_resize = cv2.resize(gray,(500,500),interpolation=cv2.INTER_CUBIC)

# # Find Canny edges
# edged = cv2.Canny(gray_resize, thresh1, 255)
ret,thresh_img = cv2.threshold(gray_resize,200 ,255,cv2.THRESH_BINARY)


contours, hierarchy = cv2.findContours(thresh_img,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img_resize,[box],0,(0,255,0))
    
    
cv2.imshow('Canny Edges After Contouring', thresh_img)

# Draw all contoursq
# -1 signifies drawing all contours

cv2.imshow('Contours', img_resize)
cv2.waitKey(0)

# import cv2
# import numpy as np

# # Let's load a simple image with 3 black squares
# img = cv2.imread(r"C:\Users\BOSS\Desktop\VT2\Data\image\IMG_20221018_172618.jpg")
# img_resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
# gray = cv2.imread(r"C:\Users\BOSS\Desktop\VT2\Data\image\IMG_20221018_172618.jpg",0)

# # Grayscale
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_resize = cv2.resize(gray,(500,500),interpolation=cv2.INTER_CUBIC)

# # Find Canny edges
# edged = cv2.Canny(gray_resize, 30, 200)


# # Finding Contours
# # Use a copy of the image e.g. edged.copy()
# # since findContours alters the image
# contours, hierarchy = cv2.findContours(edged,
# 	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# cv2.imshow('Canny Edges After Contouring', edged)

# print("Number of Contours found = " + str(len(contours)))

# # Draw all contours
# # -1 signifies drawing all contours
# cv2.drawContours(img_resize, contours, -1, (0, 255, 0), 3)

# cv2.imshow('Contours', img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
