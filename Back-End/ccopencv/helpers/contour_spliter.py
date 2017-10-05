import cv2
import numpy as np

from cont_group import cont_group

class ContourSpliter(object):

    def split(self, contour_family, categ):
    # unsigned int hi = contour_fams.size();
    # std::vector<std::vector<ContourFamily> > list_contour_fams(hi);

    # #pragma omp parallel for schedule(dynamic)
    # for(unsigned int i=0; i < hi; ++i ){
    #     signed char cat_it = categ[i];
    #     std::vector<ContourFamily> tmp_v = list_contour_fams[i];
    #     if(cat_it == 'M'){
    #         splitOneCont(contour_fams[i], tmp_v);
    #     }
    #     else if(cat_it == 'S' ){
    #         tmp_v.resize(1);
    #         tmp_v[0] = contour_fams[i];
    #     }
    #     list_contour_fams[i] = tmp_v;
    # }
#     unsigned int siz = 0;
#     for(unsigned int i=0; i < hi; ++i )
#         siz += list_contour_fams[i].size();

#     std::vector<ContourFamily> tmp_contour_fams(siz);
#     std::vector<signed char> tmp_categ(siz);

#     unsigned int k = 0;


#     for(unsigned int i=0; i < hi; ++i ){
#         unsigned int ncl = list_contour_fams[i].size();

#         for(unsigned int j=0; j < ncl; ++j ){
#             tmp_contour_fams[k] = list_contour_fams[i][j];
#             tmp_categ[k] = categ[i];
#             tmp_contour_fams[k].n_per_clust = ncl;
#             k++;

#         }
#     }

#     std::swap(tmp_contour_fams,contour_fams);
#     std::swap(tmp_categ,categ);
# }

        for idx,k in enumerate(contour_family):
            cat_it = categ[idx]
            tmp_v = list_contour_fams[idx];
            if cat_it == 'M':
                tmp_v = self.splitOneCont(k)
            elif cat_it == 'S':
                tmp_v[0] = contour_fams[idx]


    def makeWatershedLabel(self, binary, peaks_conts): # return labels
        """

        """
        _, labels = cv2.threshold(binary, 0, 1, cv2.THRESH_BINARY)
        for idx, k in peaks_conts:
            cv2.drawContours(labels, peaks_conts, idx, (idx+2,0,0), thickness = -1, lineType = 8)
        return labels

    def findPeaks(self, binary, distance_map, peaks_conts): # return distance_map and peaks
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
    # for(unsigned int j=0; j<areaCount.size();j++){
    #     areaCount[j] = 0;
    #     peakValSQ[j] = 0;
    # }

    # mask.copyTo(toUse);
    # unsigned int nc=mask.cols;
    # unsigned int nl=mask.rows;

    # /*define the peaks heigh in gray*/
    # for(unsigned int j=0; j<nl;j++){
    #     for(unsigned int i=0; i<nc;i++){
    #         char newVal =*(mask.data+j*mask.step+i*mask.elemSize());
    #         if(newVal > 1){
    #             if(peakValSQ[newVal-2] < *(gray.data+(j)*gray.step+(i)*gray.elemSize()) ){
    #                peakValSQ[newVal-2] = *(gray.data+(j)*gray.step+(i)*gray.elemSize());
    #                peakValSQ[newVal-2] = peakValSQ[newVal-2] * peakValSQ[newVal-2];
    #                center[newVal-2]=cv::Point(j,i);

    #             }
    #         }
    #     }
    # }
    # for(unsigned int j=0; j<areaCount.size();j++){
    #     maxArea[j] = maxAreaModif * peakValSQ[j]*3.1416;
    # }
    # bool on =true;
    # int iter = 0;
    # while(on){
    #     mask.copyTo(tmp);
    #     on =false;
    #     for(unsigned int j=0; j != nl; ++j){
    #         for(unsigned int i=0; i != nc; ++i){
    #             /* find pixels that are labels (mask) and unused(toUse)*/
    #             if(*(mask.data+j*mask.step+i*mask.elemSize()) > 1 && *(toUse.data+j*toUse.step+i*toUse.elemSize()) > 0){
    #                 /*for each neighbourgs*/
    #                 for(int m=-1; m != 2;++m){
    #                     for(int n=-1; n !=2;n++){
    #                         bool test = !(n == 0 && m==0 ) || (n==0 || m==0);
    #                             if( test && *(tmp.data+(j+m)*tmp.step+(i+n)*tmp.elemSize()) == 1){
    #                             switch (*(mask.data+(j+m)*mask.step+(i+n)*mask.elemSize())){
    #                                 case 0:
    #                                     break;
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
    #                                     break;
    #                                 default:
    #                                     break;
    #                             }
    #                         }
    #                     }
    #                 }
    #                 *(toUse.data+j*toUse.step+i*toUse.elemSize()) = 0;
    #                 on = true;
    #             }
    #         }
    #     }
    #     tmp.copyTo(mask);
    #     ++iter;
    # }