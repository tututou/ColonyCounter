import cv2
import numpy as np

class Predictor:

    def __init__(self):
        self.model = cv2.RTree()

    def load(self, fn):
        self.model.load(fn)

    def save(self, fn):
         self.model.save(fn)

    def train(self, features, categs):
        sample_n, var_n = features.shape
        var_types = np.array([cv2.CV_VAR_NUMERICAL] * var_n + [cv2.CV_VAR_CATEGORICAL], np.uint8)

        params = dict(
            max_depth=10,
            min_sample_count=10,
            regression_accuracy=0,
            use_surrogates=False,
            max_categories=3,
            priors = 0,
            calculate_var_importance=True,
            nactive_vars=4,
            max_num_of_trees_in_the_forest=100,
            forest_accuracy=0.01,
            termcrit_type=CV_TERMCRIT_ITER,
            )

        self.model.train(features, cv2.CV_ROW_SAMPLE, categs, varType = var_types, params = params)


    def predict(self, input_samples):
        """ For each input sample predict the output category """
        return np.float32( [self.model.predict(s) for s in input_samples] )
