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

    # inherits from step 3
    # self.input_img
    # self.cont_groups

    # def __init__(self, predictor, predictor_ps):
    #     # create contour_splitter class ??
    #     # create predictor ??
    #     # create predictor ps

    def process(self):
        """
        This step determines whether or not a contour or connected component (colony)
        is an individual colony, multiple objects or invalid.

        """
        print('starting pass two ...')
        print('self.cont_groups size: ', len(self.cont_groups))

        self.makeContourChunksVect(self.input_img)
        self.cont_groups = self.preFilterContourSize(self.cont_groups)
        feature_matrix = self.makeFeaturesMatrix(self.cont_groups)
        categ = self.predictor.predict(feature_matrix)

        # need to implement contour spliter helper class
        # <----  TODO  ----->
        self.cont_groups , categ = contour_spliter.split(self.cont_groups, categ)

        # split the contours into 2 groups (split and unsplit)
        contour_fams_split, contour_fams_unsplit = self.separateUnsplited(self.cont_groups)

        # predict categories for split contours
        contour_fams_split = self.preFilterContourSize(contour_fams_split)
        feature_mat_split = self.makeFeaturesMatrix(contour_fams_split)
        categ_split = self.predictor.predict(feature_mat_split)

        # predict categories for unsplit contours
        contour_fams_unsplit = self.preFilterContourSize(contour_fams_unsplit)
        feature_mat_unsplit = self.makeFeaturesMatrix(contour_fams_unsplit)
        categ_unsplit = self.predictor_ps.predict(feature_mat_unsplit)

        # combine contour_fams_unsplit into contour_fams_split
        # contour_fams_split.insert( contour_fams_split.end(), contour_fams_unsplit.begin(), contour_fams_unsplit.end() );
        # std::swap(contour_fams_split, contour_fams);
        self.cont_groups = contour_fams_split + contour_fams_unsplit

        # combine categ_split and unsplit
        # categ_split.insert( categ_split.end(), categ_unsplit.begin(), categ_unsplit.end() );
        # std::swap(categ_split, categ);
        categ = categ_split + categ_unsplit

        self.writeNumResults(self.cont_groups, categ);
        # m_step_result = (void*) &m_step_numerical_result

    def preFilterContourSize(self, cont_groups):
        print('preFilterContourSize...')
        tmp = []
        for k in cont_groups:
            if len(k.contours[0]) > 6:
                (x, y) = features.calculateWH(k.contour[0])
                if x > options.min_radius or y < options.max_radius:
                    tmp.append(k)
        return tmp

    def makeContourChunksVect(self, src):
        """
        Finds contours from the source image and adds to cont_groups

        input: step_image
        output: none
        """
        print('makeContourChunksVect...')
        if options.has_auto_threshold:
            _, thrd = cv2.threshold(src, options.threshold, 255, cv2.THRES_BINARY | cv2.THRESH_OTSU)
        else:
            _, thrd = cv2.threshold(src, options.threshold, 255, cv2.THRES_BINARY)

        _, contours, hierachies = cv2.findContours(thrd, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE):

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

    def writeNumResults(self, cont_fam, categ):
        """
            write results for step,
        """
        print('writeNumResults ...')
            std::vector<unsigned int> valid_idx;
        # for(unsigned int i=0;i < categ.size() ; i++)
        #     if(categ[i] == 'S')
        #         valid_idx.push_back(i);

        # DEV_INFOS(valid_idx.size());
        # m_step_numerical_result.reset(valid_idx.size());

        # for(unsigned int i=0;i < valid_idx.size() ; i++){
        #      unsigned int idx = valid_idx[i];
        #         m_step_numerical_result.add_at(OneObjectRow(contour_fams[idx],m_raw_img),i);
        #     }
        valid_idx = []
        for i,c  in enumerate(categ):
            if c = 'S':
                valid_idx.append(i)
        print('valid_idx size: ', len(valid_idx))

        for i, in enumerate(valid_idx):
            idx = valid_idx[i]
            # OneObjectRow  draws contours on raw image
            # m_step_numerical_result.add_at(OneObjectRow(contour_fams[idx], m_raw_img),i);

    def separateUnsplited(self, cont_groups):
        """ applied to self.cont_groups
        return: contour_fams_unsplit, contour_fams_split
        """
        print('separateUnsplited...')
        contour_fams_split = []
        contour_fams_unsplit = []

        for k in cont_groups:
            if k.n_per_clust > 1:
                contour_fams_split.append(k)
            else:
                contour_fams_unsplit.append(k)

        print('N splitted:', len(contour_fams_split))
        print('N unsplitted:', len(contour_fams_unsplit))

        return contour_fams_split, contour_fams_unsplit


if __name__ == '__main__':
    img_path = os.path.abspath('test_images/step1_img-bad_2.jpg')
    img = cv2.imread(img_path)
    print(img_path)
    cc = step4(img)
    cc.process()