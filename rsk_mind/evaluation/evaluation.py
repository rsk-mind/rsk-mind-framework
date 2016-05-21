from sklearn.metrics import accuracy_score

class Evaluation(object):

    """Evaluation class.

    This class is only a wrapper class for
    evaluation metrics that exist in scikit-learn.
    """

    def __init__(self):
        """Initialize an Evaluation object."""
        self.summary = {}

    def accuracy(y_true, y_predicted):
        """Compute accuracy score.

        :param y_true: a list of true labels
        :param y_predicted: a list of predicted labels as returned by a classifier
        :type y_true: list
        :type y_predicted: list
        """
        accuracy = accuracy_score(y_true, y_predicted)
        self.summary['accuracy'] = accuracy

    def precision(y_true, y_predicted):
        pass

    def recall(y_true, y_predicted):
        pass

    def F1(y_true, y_predicted):
        pass

    def roc_auc(y_true, y_score):
        pass

