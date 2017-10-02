import cv2
import matplotlib as mpl
import numpy as np
import os
mpl.use('TkAgg')
from matplotlib import pyplot as plt
import helpers.features as features
import helpers.cont_group
        
class step3(object):
        
    def __init__(self, img):
        self.input_img = img.copy()

    ##
    # The main driving method for the processing involved at this step in the algorithm
    ##
    def process(self):
        categories = []
        contour_fams = []
        step_img = np.full(
            (self.input_img.shape[0], self.input_img.shape[1]), 
            1,
            dtype = "uint8")
        self.makeContourChunksArray(self.input_img, contour_fams)

    def sizeOk(self, contour):
        if len(contour) < 7:
            return False
        return True

    ##
    # Populates the contour_fams container provided with a list of contour familiar for the provided src image.
    # Contours are taken over a variety of thresholds to score later.
    ##
    def makeContourChunksArray(self, src, contour_fams):
        # minLoc/maxLoc is a tuple of form (x, y)
        [minVal, maxVal, minLoc, maxLoc] = cv2.minMaxLoc(src)
        low = int(minVal)
        high = int(maxVal)
        assert low <= high
        limit = high - low
        hierarchies = []
        contour_chunks = []

        # Threshold image in multiples of two and see if contours exist in each threshold; get hierarchies
        for thresholdAmt in range(2, limit, 2):
            _, thrd = cv2.threshold(src, low + thresholdAmt, 255, cv2.THRESH_BINARY)
            # contours is a 2D list of (x, y), hierarchy is a list of 4 element vectors
            _, contours, hierarchy = cv2.findContours(thrd, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                for index in range(0, len(contours)):
                    contours[index] = self.reshapeContours(contours[index])
                    contour = contours[index]
                    if len(contour) > 100:
                        contours[index] = self.subsample(contour, 100)
                contour_chunks.append(np.array(contours))
                hierarchies.append(np.array(hierarchy[0])) # Gets rid of extra dime
        contour_chunks = np.array(contour_chunks)
        hierarchies = np.array(hierarchies)

        for index, chunk in enumerate(contour_chunks):
            hierarchy = hierarchies[index]
            count = 0
            chunkCount = len(chunk)
            features.calculateWH(chunk)
            while(count < chunkCount):
                holes = 0
                if hierarchy[count][0] > 0:
                    holes = hierarchy[count][0]-c-1
                else:
                    holes = chunkCount - (count+1)
                if self.sizeOk(chunk[count]):
                    print("blah")

# bool Step_3::isSizeOK(const std::vector<cv::Point>& cont) {
#     if(cont.size() < 7) {
#         return false;
#     }
#     cv::Point p = Features::calculateWH(cont);
#     if(p.x < m_min_radius || p.y > m_max_radius) {
#         return false;
#     }
#     return true;
# # }

    # for (unsigned int i = 0; i < lim; i++) {
    #     cont_chunk& chunk = all_contours_chunk[i];
    #     hier_chunk& hierarchy = all_htieras_chunk[i];
    #     unsigned int c = 0;
    #     unsigned int CC = chunk.size();
    #     while(c < CC) {
    #         /*if this is not the lastest non-hole*/
    #         unsigned int nHoles = 0;
    #         if (hierarchy[c][0] > 0) {
    #             nHoles = hierarchy[c][0]-c-1;
    #         } else {
    #             nHoles = CC - (c+1);
    #         }
    #         if (isSizeOK(chunk[c])) {
    #             #pragma omp critical
    #             {
    #                 contour_fams.push_back(ContourFamily(cont_chunk(chunk.begin() + c, chunk.begin() + c + nHoles + 1)));
    #             }
    #         }
    #         c += nHoles + 1;
    #     }
    # }

    ##
    # Reshapes the output from cv2.findContours from its 4D original structure to a 2D numpy array of (x, y) points
    # for easier processing.
    ##
    def reshapeContours(self, contours):
        out = []
        for i in range(0, len(contours)):
            (x, y) = contours[i][0]
            out.append((x, y))
        return np.array(out)

    ##
    # Reduces the number of points in a contour list to that of size_out while maintaining the
    # the overall structure of the contour via bilinear interpolation
    ##
    def subsample(self, input, size_out):
        out = []
        size_in = len(input)
        data = np.full((size_in + 1, 2), 0.0, dtype=float)
        for i in range(0, size_in):
            (x, y) = input[i]
            data[i][0] = x
            data[i][1] = y
        data[size_in][0] = data[0][0]
        data[size_in][1] = data[0][1]
        tmp_mat = cv2.resize(data, (size_out + 1, 2), cv2.INTER_LINEAR)
        for i in range(0, size_out):
            x = int(tmp_mat[0][i])
            y = int(tmp_mat[1][i])
            out.append(np.array([x, y]))
        return np.array(out)

if __name__ == '__main__':
    img_path = os.path.abspath('test_images/43.jpg')
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2GRAY)
    print(img_path)
    cc = step3(img)
    cc.process()