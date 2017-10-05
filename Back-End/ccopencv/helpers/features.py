import cv2
import math
import matplotlib as mpl
import numpy as np
import os
mpl.use('TkAgg')
from matplotlib import pyplot as plt
        
def calculateWH(contour):
    rects = cv2.minAreaRect(contour)
    rects = cv2.boxPoints(rects)
    a = calcTwoPointDist(rects[0], rects[1]) + 1
    b = calcTwoPointDist(rects[1], rects[2]) + 1
    return (max(a, b), min(a, b))

def calcTwoPointDist(p0, p1):
    (x1, y1) = p0
    (x2, y2) = p1
    ax = x1 - x2
    ax *= ax
    ay = y1 - y2
    ay *= ay
    return math.sqrt(ax + ay) / 2

##
# Consider this a property of the features module
##
def getNFeature():
    return 6+7

def smoothContours(contours):
    k = math.floor(2 * (len(contours)/40) + 1)
    if k > 99:
        k = 99
    if k > 2:
        wrap = cv2.copyMakeBorder(contours, math.floor((k-1)/2), math.floor((k-1)/2), 0, 0, cv2.BORDER_WRAP)
        blur = cv2.blur(wrap, (1, k), (-1, -1))
        return blur[math.floor((k-1)/2) : math.floor(1+len(blur)-(k-1)/2) : 1]
    else:
        return contours

def calcHullPerimArea(contour):
    hull = cv2.convexHull(contour)
    return (cv2.arcLength(contour, True), cv2.contourArea(hull))

def calcFeatures(contour_group):
    contour = smoothContours(contour_group.contours[0])
    s = len(contour_group.contours)
    num_conts = len(contour)
    assert num_conts > 6

    perim = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)

    wh = calculateWH(contour)
    pa_hull = calcHullPerimArea(contour)

    area_hole = 0.0
    perim_hole = 0.0

    for i in range(1, s):
        if len(contour_group.contours[i]) > 6:
            perim_hole += cv2.arcLength(contour_group.contours[i], True)
            area_hole += cv2.contourArea(contour_group.contours[i])

    if area_hole >= area:
        area = 1
    else:
        area -= area_hole
    perim += perim_hole
    pa_hull = (pa_hull[0] + perim_hole, pa_hull[1] - area_hole)
    assert pa_hull[1] != 0
    matData = [0.0]*getNFeature()
    p = 0
    matData[p] = perim * perim / area
    p += 1
    matData[p] = (pa_hull[1] - area) / pa_hull[1] 
    p += 1
    matData[p] = (pa_hull[0] - perim) / pa_hull[0]
    p += 1
    matData[p] = area_hole / (area + area_hole)
    p += 1
    matData[p] = perim_hole / (perim + perim_hole)
    p += 1
    matData[p] = wh[0] / (wh[1] + wh[0])
    p += 1

    hu_moments = cv2.HuMoments(cv2.moments(contour))
    for i in range(0, 7):
        matData[i + p] = hu_moments[i]
    return np.array(matData)