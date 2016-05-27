import numpy as np
import xgboost as xgb
from classifier import Classifier
from utils import separate_data_from_class


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
                'bst:max_depth': 7,
                'bst:eta': 0.3,
                'bst:subsample': 0.5,
                'silent': 0,
                'objective': 'binary:logistic',
                'nthread': 4,
                'eval_metric': 'auc'
            }
        number_of_rounds = 200

        if not self._training_dataset:
            # raise a specific error later
            raise Exception()
        else:
            data_sequence, targets_sequence = separate_data_from_class(
                    self._training_dataset)
            data = np.array(data_sequence[1])
            targets = np.array(targets_sequence[1])
            train_dmatrix = xgb.DMatrix(data, label=targets)

        if self._validation_dataset:
            vdata_sequence, vtargets_sequence = separate_data_from_class(
                    self._validation_dataset)
            vdata = np.array(vdata_sequence[1])
            vtargets = np.array(vtargets_sequence[1])
            validation_dmatrix = xgb.DMatrix(vdata, label=vtargets)
            eval_list = [(validation_dmatrix, 'evaluation'), (train_dmatrix, 'train')]
        else:
            eval_list = []

        self.model = xgb.train(parameters, train_dmatrix, number_of_rounds, eval_list)

    def save_model(self, path):
        """Save booster model.

        :param path: the path to save model to disk
        :type path: str
        """
        if self.model:
            self.model.save_model(path)
        else:
            # raise custom error later
            raise Exception()

    def load_model(self, path):
        """Load model.

        :param path: the path to load model from disk
        :type path: str
        """
        self.model = xgb.Booster({'nthread':4})
        # wrap bellow statement in a try-except statement
        # with custom exception
        self.model.load_model(path)

    def evaluate(self, threshold=0.5):
        pass

    def predict(instance):
        """Classify an instance.

        The method does not really classify but
        it outputs a probability for the positive class.

        :param instance: the instance to be classified
        :type instance: list
        """
        if not self.model:
            # raise custom error later
            raise Exception()
        else:
            to_be_classified = np.array(instance)
            _dmatrix = xgb.DMatrix(to_be_classified)
            ypredicted = self.model.predict(_dmatrix)

            return ypredicted

