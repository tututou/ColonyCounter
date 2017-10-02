import cv2
import matplotlib as mpl
import numpy as np
import os
mpl.use('TkAgg')
from matplotlib import pyplot as plt
        
def calculateWH(contour):
    print("Contour type:", type(contour))
    rects = cv2.minAreaRect(contour[0])
    print("Rects:", rects)
    print("type", type(rects))


# cv::Point2f Features::calculateWH(const std::vector<cv::Point>& contour){
#     cv::Point2f rRect[4];
#     cv::minAreaRect(contour).points(rRect);

#     float A,B;
#     A = calcTwoPointDist(rRect[0],rRect[1]) + 1;
#     B = calcTwoPointDist(rRect[1],rRect[2]) + 1;

#     return cv::Point(std::max(A,B),std::min(A,B));
# }


# inline float Features::calcTwoPointDist(const cv::Point P0,const cv::Point P1){
#         float Ax,Ay;
#         Ax = P0.x - P1.x;
#         Ax *= Ax;
#         Ay = P0.y - P1.y;
#         Ay *= Ay;
#         return sqrt(Ax + Ay) / 2;
# }
