class Classifier(object):

  """Classifier abstract class.

  This class will be sub-classed for each new
  classifier of the framework. If the user wants
  to create a custom classifier all he needs to do
  is implement the bellow methods.
  """

  def __init__(self):
    """Initialize."""
    self.model = None
    self.train_dataset = None
    self.test_dataset = None

  def set_train_dataset(self, train_set):
    """Set training dataset.

    :param train_set: the dataset to use for training
    :type train_set: Dataset
    """
    self.train_dataset = train_set

  def set_test_dataset(self, test_set):
    """Set test dataset.

    :param test_set: the dataset to use for evaluation
    :type test_set: Dataset
    """
    self.test_dataset = test_set

  def train(self, parameters={}):
    """Train the classifier.

    :param parameters: parameters given to the classifier
    :type parameters: dict
    """
    pass

  def save_model(self, path):
    """Save classifier model to disk.

    :param path: The path to disk to save the classifier model
    :type path: str
    """
    pass

  def load_model(self, path):
    """Load model to classifier from disk.

    :param path: The path to disk to load the classifier model
    :type path: str
    """
    pass

  def evaluate(self, threshold=0.5):
    """Evaluate the training algorithm.

    The method will produce some evaluation statistics.

    :param threshold: the threshold to be applied during evaluation
    :type threshold: float
    """
    pass

  def predict(instance):
    """Classify an instance.

    :param instance: the instance to be classified
    :type instance: list
    """
    pass
