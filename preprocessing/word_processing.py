from processing_string import *
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from processing_symbol import getClose

path = '../dataFiles/origImage/perfect2.jpg'
img = readImage(path)
imgMod = imgModify(img, 'open')
contour = getCont(imgMod)
lines = getString(img, contour)

# line = lines[2]
images = []
images1 = []
vert = []
for line in lines:
    line = line.copy()
    y,x = line.shape
    image = imgModify(line,"edges")

    # dilate = cv.morphologyEx(image,cv.MORPH_)
    kernel = np.ones((20,25),np.uint8)
    dilate = cv.dilate(image.copy(),kernel,iterations=1)
    kernel = np.ones((10,10),np.uint8)
    image = cv.morphologyEx(dilate,cv.MORPH_CLOSE,kernel,iterations=1)



    contours, hierarchy = cv.findContours(image.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        rect = cv.minAreaRect(cont)
        box = cv.boxPoints(rect)
        x0,y0,x1,y1 = cv.boundingRect(box)
        x1 +=x0
        # cv.rectangle(line,(x0,y0),(x1,y0+y1),(0,0,0),2)
        images.append(line[0:y,x0:x1])

#
# image = images[0:5]
# img = image[3].copy()

    close = getClose(line)
    contours, hierarchy = cv.findContours(close.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    end  = 0
    check = 0
    print("\n")
    for cont in contours:
        rect = cv.minAreaRect(cont)
        box = cv.boxPoints(rect)
        x0,y0,x1,y1 = cv.boundingRect(box)
        cv.line(line,(x0,0),(x0,y),(255,255,255),2)
        cv.line(line,(x0+x1,0),(x0+x1,y),(255,255,255),2)
        if check:
            print(end - x0,end=' ')
            end = x0
        else:
            check = 1
            end = x0
    vert.append(line)
showImage(vert)
