import cv2


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


    def makeWatershedLabel(self, binary, peaks_conts): # set = labels
        """

        """
        _, labels = cv2.threshold(binary, 0, 1, cv2.THRESH_BINARY)
        for idx, k in peaks_conts:
            cv2.drawContours(labels, peaks_conts, idx, (idx+2,0,0), thickness = -1, lineType = 8)
        return labels

    def findPeaks(self, binary, distance_map, peaks_conts):
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

    def splitOneCont(self, contour_fam):
    #     cv::Rect rect = cv::boundingRect(in.contours[0]);
    #     cv::Mat miniTmp(rect.height,rect.width,CV_8U,cv::Scalar(0));
    #     cv::drawContours(miniTmp,in.contours,-1,cv::Scalar(255),-1,8,in.hierarchies, INT_MAX, cv::Point(-rect.x,-rect.y));
    #     cv::copyMakeBorder(miniTmp,miniTmp, 4,4,4,4, cv::BORDER_CONSTANT, cv::Scalar(0));

    #     cv::Mat distance_map;
    #     cont_chunk peaks;
    #     findPeaks(miniTmp,distance_map,peaks);

    #     unsigned int n_peaks = peaks.size();
    #     cv::Mat label_mat;
    #     makeWatershedLabel(miniTmp,peaks,label_mat);
    #     watershedLike(label_mat,distance_map,n_peaks,1.6);
    #     std::vector<ContourFamily> tmp_out;
    #     tmp_out.reserve(n_peaks);
    #     for(unsigned int k=0;k != n_peaks; ++k){
    #         cv::Mat tmp;
    #         cont_chunk tmpc;
    #         cv::inRange(label_mat, k+2,k+2, tmp);
    #         cv::findContours(tmp, tmpc, cv::RETR_CCOMP, cv::CHAIN_APPROX_SIMPLE,cv::Point(rect.x-4,rect.y-4));
    #         tmp_out.push_back(ContourFamily(tmpc));
    #     }
    #     std::swap(out,tmp_out);
    # }


    def watershedLike(self):
        pass