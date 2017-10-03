import cv2
import matplotlib as mpl
import numpy as np
import os
mpl.use('TkAgg')
from matplotlib import pyplot as plt

import helpers.features as features
from helpers.cont_group import cont_group
from helpers.proc_options import proc_options as options
from helpers.predictor import Predictor
from step3 import step3

class step4(step3):

    def __init__(self, img):
        self.input_img = img.copy()


    def process(self):
        print('starting pass two ...')
        self.makeContourChunksArray(self.input_img)
        self.cont_groups = preFilterContourSize(self.cont_groups)
        feature_matrix = self.makeFeaturesMatrix(self.cont_groups)

        # need to load training data in main processer file
        # training data comes from classifier scripts + training images
        # or from the file trainnedClassifier.xml
        categ = m_predictor.predict(feature_matrix)
        # need to implement contour spliter helper class
        # m_contour_spliter.split(self.cont_groups)

        # m_predictor.predict(feature_mat,categ);

        # m_contour_spliter.split(contour_fams,categ);
        # std::vector<ContourFamily> contour_fams_split, contour_fams_unsplit;

        # separateUnsplited(contour_fams,contour_fams_unsplit,contour_fams_split);

        # cv::Mat feature_mat_split, feature_mat_unsplit;
        # std::vector<signed char> categ_split, categ_unsplit;

        # preFilterContourSize(contour_fams_split);
        # this->makeFeaturesMatrix(contour_fams_split,feature_mat_split);
        # m_predictor_ps.predict(feature_mat_split,categ_split);


        # preFilterContourSize(contour_fams_unsplit);
        # this->makeFeaturesMatrix(contour_fams_unsplit,feature_mat_unsplit);
        # m_predictor_ps.predict(feature_mat_unsplit,categ_unsplit);


        # contour_fams_split.insert( contour_fams_split.end(), contour_fams_unsplit.begin(), contour_fams_unsplit.end() );
        # std::swap(contour_fams_split,contour_fams);
        # categ_split.insert( categ_split.end(), categ_unsplit.begin(), categ_unsplit.end() );
        # std::swap(categ_split,categ);


        # writeNumResults(contour_fams,categ);
        # m_step_result = (void*) &m_step_numerical_result;

        pass

    def preFilterContourSize(self, cont_group):
        tmp = []
        for k in self.cont_groups:
            if len(k.contours[0]) > 6:
                (x, y) = features.calculateWH(k.contour[0])
                if x > options.min_radius or y < options.max_radius:
                    tmp.append(k)
        return tmp

    def makeContourChunksVect(self, src):
        if options.has_auto_threshold:
            _, thrd = cv2.threshold(src, options.threshold, 255, cv2.THRES_BINARY | cv2.THRESH_OTSU)
        else:
            _, thrd = cv2.threshold(src, options.threshold, 255, cv2.THRES_BINARY)

        _, contours, hierachies, cv2.findContours(thrd, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE):

        # look at step3 code
        contours = np.array(contours)
        hierachies = np.array(hierachies)

        for index, chunk in enumerate(contours)
            hierarchy = hierachies[index]
            count = 0
            chunkCount = len(contours)
            while(count < chunkCount):
                holes = 0
                if hierachies[count][0] > 0:
                    holes = hierachies[count][0]-count-1
                else:
                    holes = chunkCount - (count+1)
                self.cont_groups.append(cont_group( chunk[count:(count+holes+1):1] ))
                count += holes + 1

    def writeNumResults(self):
        pass

    def separateUnsplited(self):
        pass
