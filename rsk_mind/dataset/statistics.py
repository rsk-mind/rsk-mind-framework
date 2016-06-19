from numbers import Number
import numpy as np
from dataset import Dataset


class Statistics(object):
    """This class calculates several statistics for an input dataset.

    The class takes as input a `Dataset` object and calculates statistics
    such as number of instances, number of features and also individual
    statistics for every feature such as min, max, median and other values
    that may be of interest.
    """

    def __init__(self, dataset):
        """Initialize a Statistics object.

        :param dataset: the dataset to be processed
        :type dataset: Dataset
        """
        if not isinstance(dataset, Dataset):
            error = "Input {} is not an instance of Dataset class!!!".format(dataset)
            raise Exception(error)
        if not dataset:
            error = "Input {} is None!!!\nStatistics cannot be computed.".format(dataset)
            raise Exception(error)
        self.dataset = dataset
        self.header = self.dataset.header
        self.rows = self.dataset.rows
        self._statistics = {}
        # first run the general calculations
        self._calculate_general_statistics()
        # next run calculations for all attributes
        self._calculate_attributes_statistics()

    @property
    def statistics(self):
        return self._statistics

    def _calculate_general_statistics(self):
        """Calculate general statistics.

        This method simply finds the number of instances
        and the number of attributes of the dataset.
        """
        self._statistics['instances'] = len(self.rows)
        self._statistics['attributes'] = len(self.header)

    def _calculate_attributes_statistics(self):
        """Calculate statistics for all attributes.

        This method iterates over every attribute and
        calls the method `_calculate_attribute_statistics`
        """
        for index in range(0, len(self.header)):
            self._calculate_attribute_statistics(index)

    def _calculate_attribute_statistics(self, index):
        """Calculate statistics for a single attribute.

        If an attribute is numeric the following are
        calculated:
          - min
          - max
          - mean
          - standard deviation
        If an attribute is categorical(nominal) then
        the following are calculated:
          - count
          - relative_frequency

        :param index: an index in[0, len(header))
        :type index: int
        """
        column_vector = self._get_column_vector(index)
        sample_value = column_vector[1]
        attribute_name = column_vector[0]
        _type = "NUMERIC" if isinstance(sample_value, Number) else "NOMINAL"
        if _type == "NUMERIC":
            attribute_values = np.asarray(column_vector[1:])
            _min = float(attribute_values.min())
            _max = float(attribute_values.max())
            _mean = float(attribute_values.mean())
            _stdev = float(attribute_values.std())
            self._statistics[attribute_name] = {
                'type': _type,
                'min': _min,
                'max': _max,
                'mean': _mean,
                'stdev': _stdev
            }
        else:
            distinct = set(column_vector[1:])
            counts = {}
            relative_frequencies = {}
            for key in distinct:
                counts[key] = (column_vector[1:]).count(key)
                relative_frequencies[key] = counts[key] / float(self._statistics['instances'])

            self._statistics[attribute_name] = {
                'type': _type,
                'counts': counts,
                'relative_frequencies': relative_frequencies
            }

    def _get_column_vector(self, index):
        """Get a column vector.

        :param index: an index in[0, len(header))
        :type index: int
        :returns: a list of attribute values along with attribute name
        :rtype: list
        """
        column = [self.header[index]]

        # append attribute's name
        # check if this index is the last
        # then this is the class attribute (by convention)
        _class = True if (index == len(self.header) - 1) else False
        # append attribute's values
        for row in self.rows:
            if _class:
                # copy class attributes values as strings only for statistics
                column.append(str(row[index]))
            else:
                column.append(row[index])

        return column
