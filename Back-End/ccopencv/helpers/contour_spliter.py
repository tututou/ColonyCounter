import cv2
import numpy as np
from math import pi
from cont_group import cont_group

class ContourSpliter(object):

    # DONE
    def split(self, contour_groups, categ):
        assert len(contour_groups) == len(categ)
        hi = len(contour_groups)
        cont_fams_matrix = []

        for i in range(0, hi):
            category = categ[i]
            cont_list = []
            if category == "M":
                cont_list = splitOneCont(contour_groups[i])
            elif category == "S":
                cont_list = [contour_groups[i]]
            cont_fams_matrix.append(cont_list)

        contour_groups_tmp = []
        categ_tmp = []
        k = 0
        for i, item in enumerate(cont_fams_matrix):
            ncl = len(item)
            for j, group in enumerate(item):
                contour_groups_tmp.append(group)
                categ_tmp.append(categ[i])
                contour_groups_tmp[k].n_per_clust = ncl
                k += 1
        return contour_groups_tmp, categ_tmp

    # DONE
    def makeWatershedLabel(self, binary, peaks_conts): # return labels
        """

        """
        _, labels = cv2.threshold(binary, 0, 1, cv2.THRESH_BINARY)
        for idx, k in peaks_conts:
            cv2.drawContours(labels, peaks_conts, idx, (idx+2,0,0), thickness = -1, lineType = 8)
        return labels

    #DONE 
    def findPeaks(self, binary): # return distance_map and peaks
#     void ContourSpliter::findPeaks(const cv::Mat& binary, cv::Mat& distance_map, cont_chunk& peaks_conts){
#         cv::Mat tmp_mat,peaks;
#         cv::distanceTransform(binary,distance_map,CV_DIST_L2,CV_DIST_MASK_5);
#         cv::dilate(distance_map,peaks,cv::Mat(),cv::Point(-1,-1),3);
#         cv::dilate(binary,tmp_mat,cv::Mat(),cv::Point(-1,-1),3);
#         peaks = peaks - distance_map;
#         cv::threshold(peaks,peaks,0,255,cv::THRESH_BINARY);
#         peaks.convertTo(peaks,CV_8U);
#         cv::bitwise_xor(peaks,tmp_mat,peaks);
#         cv::dilate(peaks,peaks,cv::Mat(),cv::Point(-1,-1),1);
#         cv::findContours(peaks, peaks_conts, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE);
#         distance_map.convertTo(distance_map,CV_8U);
# }
        # Calculates the distance to the closest zero pixel for each pixel of the source image.
        distance_map = cv2.distanceTransform(binary, cv2.CV_DIST_L2, cv2.CV_DIST_MASK_5)

        # defult kernel in c++ when using cv::Mat()
        kernel = np.ones((3,3),np.uint8)

        # dilate increses white regions (or foreground) in image
        peaks = cv2.dilate(distance_map, kernel, anchor=(-1,-1), iterations = 3)
        tmp_mat = cv2.dilate(binary, kernel, anchor=(-1,-1), iterations = 3)

        # subtract can handel negative values
        peaks = cv2.subtract(peaks, distance_map)

        # threshold peaks
        _, peaks = cv2.threshold(peaks, 0, 255, cv2.THRESH_BINARY)

        # convert to "CV_8U" and clip
        peaks = (peaks/256).astype('uint8')
        peaks = cv2.bitwise_xor(peaks, tmp_mat)

        peaks = cv2.dilate(peaks, kernel, anchor=(-1,-1), iterations=1)
        _, peaks_conts, hierachies = cv2.findContours(peaks, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE):

        # convert to "CV_U8" and clip
        distance_map = (distance_map/256).astype('uint8')

        return distance_map, peaks

    # DONE
    def splitOneCont(self, contour_fam): # return out

        # find bonding box for contour
        rectX, rectY, rectW, rectH = cv2.boundingRect(contour_fam.contours[0])

        # create temp matrix
        miniTmp = np.full((rectH, rectW), 0, dtype="uint8")

        # draw all contours and nested contours on temp matrix
        cv2.drawContours(
            miniTmp,
            contour_fams.contours,
            -1,
            (255,0,0),
            thickness = -1,
            lineType = 8,
            hierarchy = contour_fams.hierarchies,
            maxLevel = 2,
            offset = (-rectX, -rectY)
        )
        # draw 4px constant boarder around temp matrix
        miniTmp = cv2.copyMakeBoarder(miniTmp, 4,4,4,4, cv2.BORDER_CONSTANT, 0)

        distance_map, peaks = self.findPeaks(minTmp)
        n_peaks = len(peaks)
        label_mat = self.makeWatershedLabel(miniTmp, peaks)
        self.watershedLike(label_mat, distance_map, n_peaks, 1.6)

        tmp_out = []
        for k in range(n_peaks):
            # find contours for each threshold in 2 integer jumps
            tmp = cv2.inRange(label_mat, k+2, k+2, )
             _, contours, hierachies = cv2.findContours(tmp, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE, ):
            tmp_out.append(cont_group(contours))

        return tmp_out

    def watershedLike(self, mask, gray, nlabs, maxAreaModif):
    # void ContourSpliter::watershedLike(cv::Mat &mask,cv::Mat& gray,int nlabs,double maxAreaModif){
    # /* Mask is 0 where no objects exist, 1 in undefined womes and >1 for attributed zones/labels*/
    # /* toUse is >0 for mpixel that have not yet been used as seed, and ==0 for the rest*/
    # cv::Mat toUse, tmp;
    # std::vector<int> areaCount(nlabs),peakValSQ(nlabs), maxArea(nlabs);
    # std::vector<cv::Point> center(nlabs);

    # init vectors
    areaCount = []
    peakValSQ = []
    maxArea = []
    center = []
    for i in range(len(nlabs)):
        areaCount.append(0)
        peakValSQ.append(0)
        maxArea.append(0)
        center.append((0,0))

    # for(unsigned int j=0; j<areaCount.size();j++){
    #     areaCount[j] = 0;
    #     peakValSQ[j] = 0;
    # }

    # for j in range(len(nlabs)):
    #     areaCount[j] = 0
    #     peakValSQ[j] = 0

    # mask.copyTo(toUse);
    # unsigned int nc=mask.cols;
    # unsigned int nl=mask.rows;
    toUse = mask.copy()
    nc, nl = toUse.shape

    # /*define the peaks heigh in gray*/
    # for(unsigned int j=0; j<nl;j++){
    #     for(unsigned int i=0; i<nc;i++) {
    #         char newVal = *(mask.data + j*mask.step + i*mask.elemSize());
    #         if(newVal > 1){
    #             if(peakValSQ[newVal-2] < *(gray.data+(j)*gray.step+(i)*gray.elemSize()) ){
    #                peakValSQ[newVal-2] = *(gray.data+(j)*gray.step+(i)*gray.elemSize());
    #                peakValSQ[newVal-2] = peakValSQ[newVal-2] * peakValSQ[newVal-2];
    #                center[newVal-2]=cv::Point(j,i);

    #             }
    #         }
    #     }
    # }

    for j in range(nl):
        for i in range(nc):
            newVal = mask[(j,i)]
            if newVal > 1:
                if peakValSQ[newVal-2] < gray[(j,i)]:
                    peakValSQ[newVal-2] = gray[(j,i)]
                    peakValSQ[newVal-2] = peakValSQ[newVal-2] * peakValSQ[newVal-2]
                    center[newVal-2] = (j,i)

    # for(unsigned int j=0; j<areaCount.size();j++){
    #     maxArea[j] = maxAreaModif * peakValSQ[j]*3.1416;
    # }
    for j in range(len(areaCount)):
        maxArea[j] = maxAreaModif * peakValSQ[j]*pi

    # bool on =true;
    # int iter = 0;
    # while(on){
    #     mask.copyTo(tmp);
    #     on =false;
    on = True
    count = 0
    while(on):
        tmp = mask.copy()
        on = False

    #     for(unsigned int j=0; j != nl; ++j){
    #         for(unsigned int i=0; i != nc; ++i){
        for j in range(len(nl)):
            for i in range(len(nc)):
    #             /* find pixels that are labels (mask) and unused(toUse)*/
    #            if(*(mask.data+j*mask.step+i*mask.elemSize()) > 1 && *(toUse.data+j*toUse.step+i*toUse.elemSize()) > 0){
                if mask[(j,i)] > 1 and toUse[(j,i)] > 0:
    #                 /*for each neighbourgs*/
    #                 for(int m=-1; m != 2;++m){
    #                     for(int n=-1; n !=2;n++){
                    for m in range(-1,2):
                        for n in range(-1,n):
    #                         bool test = !(n == 0 && m==0 ) || (n==0 || m==0);
                            test = not(n == 0 and m==0) or (n==0 or m==0)
    #                             if( test && *(tmp.data+(j+m)*tmp.step+(i+n)*tmp.elemSize()) == 1){
                            if test and tmp[(j+m, i+n)] == 1:
    #                             switch (*(mask.data+(j+m)*mask.step+(i+n)*mask.elemSize())){
                                    # if mask[(j+m,i+n)] == 0:
    #                                 case 0:
    #                                     break;
                                    if mask[(j+m,i+n)] == 1
    #                                 /* if the mask in markable*/
    #                                 case 1:
    #                                     /* if the neighbour value in gray is lower or equal to the target*/
    #                                     if(*(gray.data+(j+m)*gray.step+(i+n)*gray.elemSize()) <= *(gray.data+j*gray.step+i*gray.elemSize()) ){
    #                                         char newVal =*(mask.data+j*mask.step+i*mask.elemSize());
    #                                         int xd = (j+m)-center[newVal-2].x;
    #                                         int yd = (i+m)-center[newVal-2].y;
    #                                         if(areaCount[newVal-2] < maxArea[newVal-2] && xd*xd+yd*yd < maxAreaModif*peakValSQ[newVal-2]){
    #                                             *(tmp.data+(j+m)*tmp.step+(i+n)*tmp.elemSize()) = newVal;
    #                                             ++areaCount[newVal-2];
    #                                         }
    #                                     }
                                        if gray[(j+m,i+n)] <= gray[(j,i)]:
                                            newVal = mask[(j,i)]
                                            xd = (j+m) - center[newVal-2][0] # (x,y)
                                            yd = (j+m) - center[newVal-2][1]
                                            if areaCount[newVal-2] < maxArea[newVal-2] and xd*xd+yd*yd < maxAreaModif*peakValSQ[newVal-2]:
                                                tmp[(j+m,i+n)] = newVal

    #                                     break;
    #                                 default:
    #                                     break;
    #                             }
    #                         }
    #                     }
    #                 }
                    toUse[(j,i)] = 0
                    on = True
    #                 *(toUse.data+j*toUse.step+i*toUse.elemSize()) = 0;
    #                 on = true;
    #             }
    #         }
    #     }
          mask = tmp.copy()
    #     tmp.copyTo(mask);
    #     ++iter;
         count += 1 # NOT EVEN USED ?!!?
    # }