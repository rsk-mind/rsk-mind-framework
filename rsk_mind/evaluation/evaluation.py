from sklearn.metrics import (
    accuracy_score, precision_score,
    recall_score, f1_score,
    roc_auc_score
)


class Evaluation(object):
    """Evaluation class.

    This class is only a wrapper class for classification
    evaluation metrics that exist in scikit-learn.
    """

    def __init__(self):
        """Initialize an Evaluation object."""
        self._summary = {}

    @property
    def summary(self):
        """Get the calculated metrics."""
        return self._summary

    def clear_summary(self):
        """Clear the summary dictionary."""
        self._summary.clear()

    def accuracy(self, y_true, y_predicted):
        """Compute accuracy score.

        :param y_true: a list of true labels
        :param y_predicted: a list of predicted labels as returned by a classifier
        :type y_true: list
        :type y_predicted: list
        """
        accuracy = accuracy_score(y_true, y_predicted)
        self._summary['accuracy'] = accuracy

    def precision(self, y_true, y_predicted):
        """Compute precision score.

        :param y_true: a list of true labels
        :param y_predicted: a list of predicted labels as returned by a classifier
        :type y_true: list
        :type y_predicted: list
        """
        precision = precision_score(y_true, y_predicted)
        self._summary['precision'] = precision

    def recall(self, y_true, y_predicted):
        """Compute recall score.

        :param y_true: a list of true labels
        :param y_predicted: a list of predicted labels as returned by a classifier
        :type y_true: list
        :type y_predicted: list
        """
        recall = recall_score(y_true, y_predicted)
        self._summary['recall'] = recall

    def F1(self, y_true, y_predicted):
        """Compute f1 score.

        :param y_true: a list of true labels
        :param y_predicted: a list of predicted labels as returned by a classifier
        :type y_true: list
        :type y_predicted: list
        """
        f1 = f1_score(y_true, y_predicted)
        self._summary['f1'] = f1

    def roc_auc(self, y_true, y_score):
        """Compute roc-auc score.

        :param y_true: a list of true labels
        :param y_score: a list of probabilities for the positive class, as returned by a classifier
        :type y_true: list
        :type y_score: list
        """
        auc = roc_auc_score(y_true, y_score)
        self._summary['auc'] = auc
