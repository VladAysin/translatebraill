from processing_string import *
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from processing_symbol import getClose

path = '../dataFiles/origImage/perfect2.jpg'
lines = returnLines(path)

# # line = lines[2]
# images = []
# images1 = []
# vert = []
# coordsX = []
# for line in lines:
#     line = line.copy()
#     y,x = line.shape
#     image = imgModify(line,"edges")
#
#     # dilate = cv.morphologyEx(image,cv.MORPH_)
#     kernel = np.ones((20,20),np.uint8)
#     dilate = cv.dilate(image.copy(),kernel,iterations=1)
#     kernel = np.ones((10,10),np.uint8)
#     image = cv.morphologyEx(dilate,cv.MORPH_CLOSE,kernel,iterations=1)
#
#
#
#     contours, hierarchy = cv.findContours(image.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     contours = contours[::-1]
#     check = 0
#     for cont in contours:
#         rect = cv.minAreaRect(cont)
#         box = cv.boxPoints(rect)
#         x0,y0,x1,y1 = cv.boundingRect(box)
#         x1 +=x0
#         if not check:
#             cv.rectangle(line,(x0,0),(x1+x0,y),(0,0,0),2)
#             check = 1
#         else:
#             cv.rectangle(line,(x0,0),(x1+x0,y),(255,255,255),2)
#     images.append(line)
#
# #
# image = images[0:5]
# img = image[3].copy()

#     close = getClose(line)
#     contours, hierarchy = cv.findContours(close.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     end  = 0
#     check = 0
#     contours = contours[::-1]
#     for cont in contours:
#         rect = cv.minAreaRect(cont)
#         box = cv.boxPoints(rect)
#         x0,y0,x1,y1 = cv.boundingRect(box)
#         # cv.line(line,(x0,0),(x0,y),(255,255,255),2)
#         # cv.line(line,(x0+x1,0),(x0+x1,y),(255,255,255),2)
#         if not check:
#             cv.rectangle(line,(x0,0),(x1+x0,y),(0,0,0),2)
#             check = 1
#         else:
#             cv.rectangle(line,(x0,0),(x1+x0,y),(255,255,255),2)
#         coordsX.append([x0,x0+x1])
#
#     vert.append(line)
# showImage(vert)
# showImage(images)

def getSred(contours):
    sredX1 = 0
    sred_ = 0
    check = 1
    for cont in contours:
        x0,_,x1,_ = cont
        sredX1 += (x1**2)/len(contours)
        if check:
            check = 0
            backX = x0+x1
        else:
            sred_ = ((x0-backX)**2)/len(contours)
            backX = x0+x1

    sredX1 = int(sredX1**0.5)
    sred_ = int(sred_**0.5)
    print(sredX1,sred_)



line = lines[0]
img = line.copy()
y,x = img.shape
img = imgModify(img,'edges')
kernel = np.ones((100,5),np.uint8)

dilate = cv.dilate(img,kernel, iterations=1)
dilate1 = cv.dilate(img,kernel, iterations=2)

conts = getCont(dilate1)
check = 0

getSred(conts)
for cont in conts:
    x0,y0,x1,y1 = cont

    if not check:
        cv.line(line,(x0,0),(x0,y),(0,255,255),2)
        check = 1
    else:
        cv.line(line,(x0,0),(x0,y),(255,255,255),2)


test = drawRect(img, conts)
showImage(cv.cvtColor(line,cv.COLOR_BGR2RGB))
