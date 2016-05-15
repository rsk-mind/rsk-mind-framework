from nose.tools import assert_equals
from rsk_mind.dataset import Dataset
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

    class_vector = [str(row[len(self.header) - 1]) for row in self.rows]

    assert_equals(stats_dictionary[self.header[len(self.header) - 1]]['counts']['1'],
                  class_vector.count('1'))

    assert_equals(stats_dictionary[self.header[len(self.header) - 1]]['counts']['0'],
                  class_vector.count('0'))

    assert_equals(stats_dictionary[self.header[len(self.header) - 1]]['type'], "NOMINAL")
