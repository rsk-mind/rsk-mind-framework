import numpy as np
import xgboost as xgb
from classifier import Classifier


class XgboostClassifier(Classifier):

    def __init__(self):
        """Initialize an xgboost classifier."""
        super(XgboostClassifier, self).__init__()

    def train(self, parameters={}):
        """Train the classifier.

        The method trains a model using xgboost's algorithm
        which is a gradient boosting trees implementation.
        """
        if not parameters:
            parameters = {
                'bst:max_depth':7,
                'bst:eta': 0.3,
                'bst:subsample':0.5,
                'silent':1,
                'objective':'binary:logistic',
                'nthread':4,
                'eval_metric':'auc'
            }
        number_of_rounds = 200

        dtrain = None
        if not self._training_dataset:
            # raise a specific error later
            raise Exception()

        eval_list = []
        if self._validation_dataset:




