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