import cv2
import numpy as np
import os
from sklearn.externals import joblib

from ccopencv.helpers.predictor import Predictor
from ccopencv.helpers.proc_options import proc_options as options
from ccopencv.step1 import step1
from ccopencv.step3 import step3
from ccopencv.step4 import step4


class Processor(object):

    def __init__(self, img64):
        self.img_base64 = img64
        self.results = None
        self.step_results = None
        cur_path = os.path.dirname(__file__)
        filename = os.path.join(cur_path, 'classifier', 'rTree_trained_model.pkl')
        filename_ps = os.path.join(cur_path, 'classifier', 'rTree_trained_model_ps.pkl')
        print('path to trained model: ',filename)
        print('path to trained model: ',filename_ps)
        self.predictor = joblib.load(filename) # ?
        self.predictor_ps = joblib.load(filename_ps)


    def runAll(self, extension):
        """ run through each step to process image """
        img_arr = np.fromstring(self.img_base64, dtype=np.uint8)
        self.img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

        process1 = step1(self.img)
        step_res = process1.process()
        cv2.imwrite('step1res.' + extension, step_res, [cv2.IMWRITE_JPEG_QUALITY, 100])

        process2 = step3(step_res, self.predictor)
        step_res = process2.process()
        cv2.imwrite('step2res.' + extension, step_res, [cv2.IMWRITE_JPEG_QUALITY, 100])

        process3 = step4(step_res, self.predictor, self.predictor_ps)
        res = process3.process()
        return res

    def writeResults(self):
        """ print out resutls """
        pass

if __name__ == '__main__':
    img_path = os.path.abspath('test_images/43.jpg')
    img = cv2.imread(img_path)
    print(img_path)
    p = Processor()
    p.runAll()
