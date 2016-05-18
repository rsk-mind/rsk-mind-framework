from random import (uniform, randint)
from nose.tools import assert_equals
from rsk_mind.dataset import (Dataset, Splitter)


class TestSplitter(object):

  def setUp(self):
    header = []
    for i in range(4):
      header.append('f{}'.format(i))
    header.append('target')

    rows = []
    for row_index in range(100):
      row = []
      for column_index in range(len(header) - 1):
        row.append(uniform(-10, 10))
      row.append(randint(0, 1))
      rows.append(row)

    self.dataset = Dataset(header, rows)
    self.dataset.transformed_header = list(header)
    self.dataset.transformed_rows = list(rows)
    self.original_size = len(rows)

  def tearDown(self):
    del self.dataset

  def test_default_percentages(self):
    _splitter = Splitter(self.dataset)

    expected_test_dataset_length = _splitter.test_p * self.original_size
    assert_equals(len(_splitter.test_dataset.transformed_rows),
                  expected_test_dataset_length)

    expected_validation_dataset_length = _splitter.validation_p * self.original_size
    assert_equals(len(_splitter.validation_dataset.transformed_rows),
                  expected_validation_dataset_length)

  def test_invalid_percentages(self):
    error = None
    try:
      _splitter = Splitter(self.dataset, 0.3, 0.3)
    except Exception, e:
      error = e
    assert_equals(isinstance(error, Exception), True)
    assert_equals(error.message, "The sum of test and validation "
                  "percentages cannot exceed 0.3")

  def test_valid_percentages(self):
    _splitter = Splitter(self.dataset, 0.15, 0.15)
    expected_test_dataset_length = _splitter.test_p * self.original_size
    assert_equals(len(_splitter.test_dataset.transformed_rows),
                  expected_test_dataset_length)

    expected_validation_dataset_length = _splitter.validation_p * self.original_size
    assert_equals(len(_splitter.validation_dataset.transformed_rows),
                  expected_validation_dataset_length)
