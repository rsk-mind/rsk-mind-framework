from nose.tools import assert_equals
import os
from rsk_mind.dataset import Dataset
from rsk_mind.datasource import CSVDataSource
from rsk_mind.dataset import Statistics


class TestStatistics(object):

  """Test class for dataset.statistics.
  """

  def setUp(self):
    """Set up dummy data.
    """
    self.header = ['f1', 'f2', 'f3', 'class']
    self.rows = [
        [0.2, 0.54, 0.21, 1],
        [0.7, 0.63, 0.17, 0],
        [0.4, 0.91, 0.22, 1],
        [0.16, 0.85, 0.3, 1]
    ]
    self.in_path = os.path.join(os.getcwd(), 'tests/files/dataset_statistics_test.csv')

  def test_init_statistics_none(self):
    """Initialize Statistics with None.
    """
    error = None
    dataset = None

    try:
      Statistics(dataset)
    except Exception, e:
      error = e

    assert_equals(isinstance(error, Exception), True)

  def test_init_statistics_no_dataset_instance(self):
    """Initialize Statistics with a list.
    """
    error = None
    dataset = ['a', 'list', 'is', 'no', 'Dataset', 'instance']

    try:
      Statistics(dataset)
    except Exception, e:
      error = e

    assert_equals(isinstance(error, Exception), True)

  def test_init_statistics(self):
    """Initialize Statistics with a Dataset instance.
    """
    error = None
    dataset = Dataset(self.header, self.rows)

    try:
      Statistics(dataset)
    except Exception, e:
      error = e

    assert_equals(error, None)

  def test_get_statistics(self):
    """Get statistics dictionary from dataset.
    """
    dataset = Dataset(self.header, self.rows)
    dataset_stats = Statistics(dataset)

    stats_dictionary = dataset_stats.statistics

    assert_equals(isinstance(stats_dictionary, dict), True)

    assert_equals('instances' in stats_dictionary, True)
    assert_equals(stats_dictionary['instances'], len(self.rows))

    assert_equals('attributes' in stats_dictionary, True)
    assert_equals(stats_dictionary['attributes'], len(self.header))

    class_vector = [float(row[len(self.header) - 1]) for row in self.rows]

    target_stats = stats_dictionary[self.header[len(self.header) - 1]]

    assert_equals("type" in target_stats, True)
    assert_equals("max" in target_stats, True)
    assert_equals("min" in target_stats, True)
    assert_equals("mean" in target_stats, True)
    assert_equals("stdev" in target_stats, True)

    assert_equals(target_stats["type"], "NUMERIC")
    assert_equals(target_stats["max"], max(class_vector))
    assert_equals(target_stats["min"], min(class_vector))
    assert_equals(target_stats["mean"],
                  sum(class_vector) / float(len(class_vector)))

  def test_csv_dataset_statistics(self):
    data = CSVDataSource(self.in_path, target='CANCER_POSSIBILITY').read()
    dataset_stats = Statistics(data)

    stats_dictionary = dataset_stats.statistics

    expected_numeric_attributes = 3
    expected_nominal_attributes = 2

    attribute_types_hash = {}

    for k in stats_dictionary:
      v = stats_dictionary[k]
      if isinstance(v, dict):
        _type = v['type']
        if _type in attribute_types_hash:
          attribute_types_hash[_type] += 1
        else:
          attribute_types_hash[_type] = 1

    assert_equals(attribute_types_hash['NOMINAL'], expected_nominal_attributes)
    assert_equals(attribute_types_hash['NUMERIC'], expected_numeric_attributes)