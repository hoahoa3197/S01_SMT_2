import cv2
import math
import numpy as np
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

sizeofscr = 500

blank_image = np.zeros((sizeofscr, sizeofscr, 3), np.uint8)
start_point = (460, 320)     #yellow_point
dest_point = (150, 145)    #green_point
res_point=None              #red_point
# cv2.circle(blank_image, start_point, 10, (0, 255, 0), -1)
# cv2.circle(blank_image, dest_point, 10, (0, 255, 255), -1)
# theta = np.arctan2(start_point[1]-dest_point[1], start_point[0]-dest_point[0])
# endpt_x = int(start_point[0] - 1000*np.cos(theta))
# endpt_y = int(start_point[1] - 1000*np.sin(theta))
# end_points= (endpt_x, endpt_y)
# print(end_points)


# cv2.line(blank_image, (start_point[0], start_point[1]), (endpt_x, endpt_y), 255, 2)

# Points=linePoints(start_point[0],start_point[1],end_points[0],end_points[1])
# for point in Points:
#     if abs(get_distance(dest_point,point)-get_distance(start_point,dest_point))<=0.5:
#         if point!=start_point:
#             res_point=point
cv2.circle(blank_image,res_point,10,(0,0,255),-1)
contours = cv2.findContours(blank_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]
contour_img = np.zeros_like(blank_image)
cv2.fillPoly(contour_img, contours, 255)
cv2.imshow("test", blank_image)
cv2.waitKey(0)