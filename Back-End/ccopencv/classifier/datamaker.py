import cv2
import numpy as np
import os
import sys


sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
from helpers import features
from helpers.cont_group import cont_group


class DataMaker(object):
    """ Train a classification model with trainning images """

    def __init__(self, path_to_images):
        # get list of training files
        self.taining_files = self.makefileList(path_to_images)
        self.train_features = []
        self.train_labels = []

    def makefileList(self, path):
        print(os.path.dirname(path))
        l = [ os.path.abspath( os.path.join(os.path.dirname(path), f)) for f in os.listdir(path) if f.endswith(".png")]
        print(l)
        return l

    def findCategoryFromName(self, file_name):
        if file_name.startswith('Mult_'):
            categ = 'M'
        elif file_name.startswith('Neg_'):
            categ = 'N'
        elif file_name.startswith('Sing_'):
            categ = 'S'
        return categ

    def makeData(self):
        """
            create feature vector and category vector
        """
        for f in self.taining_files:
            file_path = os.path.abspath(f)
            print(file_path)
            src_img = cv2.imread(file_path, 0)
            # cv2.imshow('src_img',src_img)
            # cv2.waitKey(0)
            file_name = os.path.split(file_path)[1]
            categ = self.findCategoryFromName(file_name)
            print(file_name, categ)

            img_0 = src_img.copy()
            for i in range(-1,3):
                print(i)
                # flip image about horizontal and vertial axies
                img = cv2.flip(img_0, i)
                # cv2.imshow('img_{}'.format(i), img)
                # cv2.waitKey(0)
                for j in range(4):
                    print(j)
                    img = cv2.transpose(img, img)
                    img = cv2.flip(img, 0)
                    # cv2.imshow('img_{}_{}'.format(i,j), img)
                    cont_fams = self.makeContourChunksVect(img)
                    cont_fams = self.preFilterContourSize(cont_fams)
                    train_features = self.makeFeaturesMatrix(cont_fams)
                    self.train_features.extend(train_features)

                    for k in cont_fams:
                        self.train_labels.append(categ)

    def makeFeaturesMatrix(self, cont_groups):
        print('makeFeaturesMatrix...')
        n = len(cont_groups)
        n_features = features.getNFeature()
        out = []
        for i in range(0, n):
            row = features.calcFeatures(cont_groups[i])
            out.append(np.array(row))
        return np.array(out)


    def makeContourChunksVect(self, img):
        print('makeContourChunksVect...')
    #     cont_chunk contours_chunk;
    #     hier_chunk hieras_chunk;
    #     cv::Mat thrd;
    #     cv::threshold(src,thrd,128,255,cv::THRESH_BINARY);
    #     cv::findContours(thrd, contours_chunk, hieras_chunk, cv::RETR_CCOMP, cv::CHAIN_APPROX_SIMPLE);
    #     unsigned int c=0;
    #     unsigned int CC = contours_chunk.size();

    #     while ( c < CC){
    #         /*if this is not the lastest non-hole*/
    #         unsigned int nHoles = 0;
    #         if( hieras_chunk[c][0] > 0)
    #             nHoles = hieras_chunk[c][0]-c-1;
    #         else
    #             nHoles = CC - (c+1);
    #         contour_fams.push_back(ContourFamily(cont_chunk(contours_chunk.begin()+c,contours_chunk.begin()+c+nHoles+1)));
    #         c += nHoles+1;
    #     }
    # }

        _, thrd = cv2.threshold(img, 128,255, cv2.THRESH_BINARY)
        _, contours, hierachies = cv2.findContours(thrd, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        # look at step3 code

        contours = np.array(contours)
        print(contours)
        hierachies = np.array(hierachies)
        cont_groups = []

        # print(hierachies[0]) # list of list
        count = 0
        chunkCount = len(contours)
        while(count < chunkCount):
            # print('count: ', count)
            # print('chunkCount: ', chunkCount)
            holes = 0
            if hierachies[0][count][0] > 0:
                holes = hierachies[0][count][0] - count-1
            else:
                holes = chunkCount - (count+1)
            cont_groups.append(cont_group( contours[count:(count+holes+1):1] ))
            count += holes + 1
        # print('leng cont_groups: ', len(cont_groups))
        return cont_groups


    def preFilterContourSize(self, cont_groups):
        print('preFilterContourSize...')
        tmp = []
        for k in cont_groups:
            if len(k.contours[0]) <= 6:
                continue
            else:
                tmp.append(k)
        return tmp

if __name__ == '__main__':
    if __package__ is None:
        sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
        from helpers import features
        from helpers.cont_group import cont_group
    else:
        from ..helpers import features
        from ..helpers.cont_group import cont_group

    path = 'training-set1/'
    dm = DataMaker(path)
    dm.makeData()

    print('train_features: ',len(dm.train_features))
    print('train_labels:', len(dm.train_labels))

    print('train_label[100]: ', dm.train_labels[100])
    print('train_features[100]: ', dm.train_features[100])




