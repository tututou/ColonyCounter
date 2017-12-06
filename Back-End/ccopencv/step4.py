import cv2
import numpy as np
import os

from ccopencv.helpers.contour_spliter import ContourSpliter
import ccopencv.helpers.features as features
from ccopencv.helpers.cont_group import cont_group
from ccopencv.helpers.proc_options import proc_options as options
from ccopencv.step3 import step3

class step4(step3):

    # inherits from step 3
    # self.input_img
    # self.cont_groups
    def __init__(self, step_img, predictor, predictor_ps, original):
        self.input_img = step_img.copy()
        self.original_img = original.copy()
        self.cont_groups = []
        self.predictor = predictor
        self.predictor_ps = predictor_ps
        self.contour_spliter = ContourSpliter()


    def process(self):
        """
        This step determines whether or not a contour or connected component (colony)
        is an individual colony, multiple objects or invalid.

        """
        print('starting step4...')

        # make initial contour category predictions
        self.makeContourChunksVect(self.input_img)
        self.cont_groups = self.preFilterContourSize(self.cont_groups)
        feature_matrix = self.makeFeaturesMatrix(self.cont_groups)
        categ = self.predictor.predict(feature_matrix)

        # split contour groups into single or multiple colonies
        self.cont_groups , categ = self.contour_spliter.split(self.cont_groups, categ)

        # split the contours into 2 groups (split and unsplit)
        # this could use some work as it missed some multiple colony groups
        contour_fams_split, contour_fams_unsplit = self.separateUnsplited(self.cont_groups)

        # predict category labels ('N', 'S', 'M') for split contours
        contour_fams_split = self.preFilterContourSize(contour_fams_split)
        feature_mat_split = self.makeFeaturesMatrix(contour_fams_split)
        if len(feature_mat_split) > 0:
            categ_split = self.predictor.predict(feature_mat_split)
        else:
            categ_split = np.array([])

        # predict categories for ('N', 'S', 'M') unsplit contours
        contour_fams_unsplit = self.preFilterContourSize(contour_fams_unsplit)
        feature_mat_unsplit = self.makeFeaturesMatrix(contour_fams_unsplit)
        if len(feature_mat_unsplit) > 0:
            categ_unsplit = self.predictor_ps.predict(feature_mat_unsplit)
        else:
            categ_unsplit = np.array([])

        # combine results back into
        self.cont_groups = np.concatenate((contour_fams_split, contour_fams_unsplit))
        categ = np.concatenate((categ_split, categ_unsplit), axis=0)

        return self.writeNumResults(self.cont_groups, categ)


    def preFilterContourSize(self, cont_groups):
        """ Filter out contours with sizes less than min_radius  or greater than max_radius """
        tmp = []
        for k in cont_groups:
            if len(k.contours[0]) > 6:
                (x, y) = features.calculateWH(k.contours[0])
                if x > options.min_radius or y < options.max_radius:
                    tmp.append(k)
        return tmp

    def makeContourChunksVect(self, src):
        """
        Finds contours from the source image and adds to cont_groups

        input: step_image
        output: self.cont_groups
        """
        if options.has_auto_threshold:
            _, thrd = cv2.threshold(src, options.threshold, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        else:
            _, thrd = cv2.threshold(src, options.threshold, 255, cv2.THRESH_BINARY)

        _, contours, hierachies = cv2.findContours(thrd, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))

        # reshape contours to condense array
        for index in range(0, len(contours)):
            contours[index] = self.reshapeContours(contours[index])

        contours = np.array(contours)
        hierachies = np.array(hierachies[0])

        count = 0
        chunkCount = len(contours)

        while(count < chunkCount):
            holes = 0
            if hierachies[count][0] > 0:
                holes = hierachies[count][0]-count-1
            else:
                holes = chunkCount - (count + 1)
            self.cont_groups.append(cont_group( contours[count:(count+holes+1):1] ))
            count += holes + 1

    def writeNumResults(self, cont_fam, categ):
        """
            write results for step,
        """
        # print(cont_fam[0].contours)
        # print(type(cont_fam))
        valid_idx = []

        h, w = self.input_img.shape
        tmp_mat = np.full((h,w), 0, dtype='uint8')

        for i,c  in enumerate(categ):
            if c == 'S' or c=='M':
                valid_idx.append(i)

        for k in cont_fam:
            cv2.drawContours(self.original_img, k.contours, -1, (80,244,66), thickness = 3, lineType = 8)

        return len(valid_idx), self.original_img

    def separateUnsplited(self, cont_groups):
        """ applied to self.cont_groups
        return: contour_fams_unsplit, contour_fams_split
        """
        contour_fams_split = []
        contour_fams_unsplit = []

        for k in cont_groups:
            if k.n_per_clust > 1:
                contour_fams_split.append(k)
            else:
                contour_fams_unsplit.append(k)

        return contour_fams_split, contour_fams_unsplit


if __name__ == '__main__':
    img_path = os.path.abspath('test_images/step3_img-contours.jpg')
    img = cv2.imread(img_path)
    print(img_path)
    cc = step4(img)
    cc.process()
