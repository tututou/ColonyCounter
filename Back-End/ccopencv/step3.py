import cv2
import numpy as np
import os
from sklearn.externals import joblib

import ccopencv.helpers.features as features
from ccopencv.helpers.cont_group import cont_group
from ccopencv.helpers.proc_options import proc_options as options

class step3(object):

    def __init__(self, img):
        self.input_img = img.copy()
        self.cont_groups = []
        cur_path = os.path.dirname(__file__)
        filename = os.path.join(cur_path, 'classifier', 'rTree_trained_model.pkl')
        filename_ps = os.path.join(cur_path, 'classifier', 'rTree_trained_model_ps.pkl')
        print('path to trained model: ',filename)
        print('path to trained model: ',filename_ps)
        self.predictor = joblib.load(filename) # ?
        self.predictor_ps = joblib.load(filename_ps)

    ##
    # The main driving method for the processing involved at this step in the algorithm
    ##
    def process(self):
        self.step_img = np.full(
            (self.input_img.shape[0], self.input_img.shape[1]),
            1,
            dtype = "uint8")
        self.makeContourChunksArray(self.input_img)
        feature_matrix = self.makeFeaturesMatrix(self.cont_groups)
        categ = self.predictor.predict(feature_matrix)
        self.drawAllValidContours(self.cont_groups, categ)
        return self.step_img


    def drawAllValidContours(self, cont_groups, categories):
        print("Entering drawAllValidContours")
        for i in range(0, len(cont_groups)):
            contours = cont_groups[i].contours
            print
            hierarchies = cont_groups[i].hierarchies
            rectX, rectY, rectW, rectH = cv2.boundingRect(contours[0])
            rect_mat = np.full(
                (rectH, rectW),
                0,
                dtype="uint8")
            if categories[i] != "N":
                cv2.drawContours(rect_mat, contours, -1, (255,0,0), thickness = -1, lineType = 8, maxLevel = 2, offset = (-rectX, -rectY))
                self.step_img[rectY:(rectY+rectH), rectX:(rectX+rectW)] += rect_mat
                # cv2.drawContours(rect_mat, contours, -1, (255,0,0), -1, 8, hierarchies, 2, (-rectX, -rectY))
                # self.step_img[rectY:(rectY+rectH), rectX:(rectX+rectW)] = self.step_img[rectY:(rectY+rectH), rectX:(rectX+rectW)] + rect_mat
            # cv2.drawContours(rect_mat, contours, -1, (255,0,0), thickness = -1, lineType = 8, maxLevel = 2, offset = (-rectX, -rectY))
            # self.step_img[rectY:(rectY+rectH), rectX:(rectX+rectW)] += rect_mat


    def makeFeaturesMatrix(self, cont_groups):
        print("Entering makeFeaturesMatrix")
        n = len(cont_groups)
        n_features = features.getNFeature()
        out = []
        for i in range(0, n):
            row = features.calcFeatures(cont_groups[i])
            out.append(np.array(row))
        return np.array(out)

    ##
    # Populates the contour_fams container provided with a list of contour familiar for the provided src image.
    # Contours are taken over a variety of thresholds to score later.
    ##
    def makeContourChunksArray(self, src):
        print("Entering makeContourChunksArray")
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
            while(count < chunkCount):
                holes = 0
                if hierarchy[count][0] > 0:
                    holes = hierarchy[count][0]-count-1
                else:
                    holes = chunkCount - (count+1)
                if self.sizeOk(chunk[count]):
                    self.cont_groups.append(cont_group( chunk[count:(count+holes+1):1] ))
                count += holes + 1

    def sizeOk(self, contour):
        if len(contour) < 7: # Magic numbers -__-
            return False
        (x, y) = features.calculateWH(contour)
        if x < options.min_radius or y < options.min_radius or x > options.max_radius or y > options.max_radius:
            return False
        return True

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
    img_path = os.path.abspath('test_images/step1_img-good_3.jpg')
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2GRAY)

    cc = step3(img)
    cc.process()
