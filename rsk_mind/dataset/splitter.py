from random import shuffle
from math import ceil
from dataset import Dataset


class Splitter(object):

  """The Splitter class.

  The class serves to split a dataset.
  """

  def __init__(self, dataset,
               test_percentage=0.1,
               validation_percentage=0.1):
    self.test_p = test_percentage
    self.validation_p = validation_percentage
    self.dataset = dataset
    self._test_dataset = None
    self._validation_dataset = None
    self._train_dataset = None
    self._split_dataset()

  @property
  def test_dataset(self):
    return self._test_dataset

  @property
  def validation_dataset(self):
    return self._validation_dataset

  @property
  def training_dataset(self):
    return self._train_dataset

  def _split_dataset(self):
    """Split the original dataset.

    Split the dataset into test, validation
    and training according to given percentages.
    """
    try:
      self._ensure_max_percentages_sum()

      dataset_size = len(self.dataset.transformed_rows)
      indexes = range(dataset_size)
      shuffle(indexes)

      # create the test dataset
      if self.test_p != 0:
        test_size = int(ceil(self.test_p * dataset_size))
        test_indexes = self._pop_first_k_elements(test_size, indexes)
        transformed_rows = []
        for _index in test_indexes:
          transformed_rows.append(self.dataset.transformed_rows[_index])

        self._test_dataset = Dataset([], [])
        self._test_dataset.transformed_header = self.dataset.transformed_header
        self._test_dataset.transformed_rows = transformed_rows

      # create the validation dataset
      if self.validation_p != 0:
        validation_size = int(ceil(self.validation_p * dataset_size))
        validation_indexes = self._pop_first_k_elements(validation_size, indexes)
        transformed_rows = []
        for _index in validation_indexes:
          transformed_rows.append(self.dataset.transformed_rows[_index])

        self._validation_dataset = Dataset([], [])
        self._validation_dataset.transformed_header = self.dataset.transformed_header
        self._validation_dataset.transformed_rows = transformed_rows

      # create train dataset
      transformed_rows = []
      for _index in indexes:
        transformed_rows.append(self.dataset.transformed_rows[_index])
      self._train_dataset = Dataset([], [])
      self._train_dataset.transformed_header = self.dataset.transformed_header
      self._train_dataset.transformed_rows = transformed_rows

    except Exception, e:
      raise e

  def _ensure_max_percentages_sum(self):
    """Check sum of percentages.

    Ensure that the sum of test and validation percentages
    does not exceed 0.30. For some algorithms a set of 70%
    of the given data might be enough for training.
    """
    # maybe 0.3 can be in a configuration file
    if round(self.test_p + self.validation_p) > 0.3:
      raise Exception(
          "The sum of test and validation percentages cannot exceed 0.3")

  def _pop_first_k_elements(self, k, items):
    """Pop the first k elements.

    :param k: the number of elements to pop
    :type k: int
    :param items: the given list of elements
    :type items: list
    """
    removed = []
    times = 0
    while times < k:
      removed.append(items.pop(0))
      times += 1

    return removed
