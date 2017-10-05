import cv2
import matplotlib as mpl
import numpy as np

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
        # instantiate predictor ? load data ?


    def runAll(self, extension):
        """ run through each step to process image """
        img_arr = np.fromstring(self.img_base64, dtype=np.uint8)
        self.img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        process1 = step1(self.img)
        step_res = process1.process()
        cv2.imwrite('step1res.' + extension, step_res, [cv2.IMWRITE_JPEG_QUALITY, 100])
        process2 = step3(step_res)
        step_res = process2.process()
        cv2.imwrite('step2res.' + extension, step_res, [cv2.IMWRITE_JPEG_QUALITY, 100]) 
        _, contours, hierarchy = cv2.findContours(step_res, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        return 56

    def writeResults(self):
        """ print out resutls """
        pass

if __name__ == '__main__':
    img_path = os.path.abspath('test_images/43.jpg')
    img = cv2.imread(img_path)
    print(img_path)
    p = Processor()
    p.runAll()