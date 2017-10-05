import cv2
import matplotlib as mpl
import numpy as np

from .helpers.predictor import Predictor
from .helpers.proc_options import proc_options as options
from .step1 import step1
from .step3 import step3
from .step4 import step4


class Processor(object):

    def __init__(self, img):
        self.img_base64 = img
        self.results = None
        self.step_results = None
        # instantiate predictor ? load data ?


    def runAll(self):
        """ run through each step to process image """
        img_arr = np.fromstring(self.img_base64, np.uint8)
        self.img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        cv2.imshow(self.img)
        cv2.waitKey(0)
        # run step1
        # run step3
        # run step4


    def writeResults(self):
        """ print out resutls """
        pass

if __name__ == '__main__':
    img_path = os.path.abspath('test_images/43.jpg')
    img = cv2.imread(img_path)
    print(img_path)
    p = Processor()
    p.runAll()