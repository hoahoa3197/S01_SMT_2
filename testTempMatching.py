import cv2
import numpy as np

image = cv2.imread(r'C:\Users\BOSS\Desktop\B01-SMT\Data\image\temp2.png')
template = cv2.imread(r'C:\Users\BOSS\Desktop\B01-SMT\Data\image\temp\Screenshot_1.png')
(templateHeight, templateWidth) = template.shape[:2]

matchResult = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
(_, _, minLoc, maxLoc) = cv2.minMaxLoc(matchResult)

topLeft = maxLoc
botRight = (topLeft[0] + templateWidth, topLeft[1] + templateHeight)
roi = image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]
 
mask = np.zeros(image.shape, dtype = "uint8")
image = cv2.addWeighted(image, 0.25, mask, 0.75, 0)

image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
 
cv2.imwrite("matchedTemplate.png", image)