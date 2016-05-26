from nose.tools import assert_equals
from rsk_mind.dataset import Dataset
from rsk_mind.utils import *
import os


class TestUtils:

    def setUp(self):
        header = ['a', 'b', 'target']
        rows = [
            [5, 2, 1],
            [10.0, 7, 0],
            [3, 2, 1],
            [3, 4, 0]
        ]
        transformed_header = ['a', 'b', 'ratio', 'target']
        transformed_rows = [
            [5, 2, 5/2.0, 1],
            [10.0, 7, 10.0/7.0, 0],
            [3, 2, 3/2.0, 1],
            [3, 4, 3/4.0, 0]
        ]
        self.dataset = Dataset(header, rows)
        self.dataset.transformed_header = transformed_header
        self.dataset.transformed_rows = transformed_rows

        self.str_list = ['1.0', '0.0', '1', '0']

    def tearDown(self):
        del self.dataset
        del self.str_list

    def test_strings_to_numeric(self):
        result = strings_to_numeric(self.str_list)
        assert_equals(type(result), list)
        assert_equals(type(result[0][1]), list)
        assert_equals(result[0][1], [1, 0, 1, 0])

    def test_get_column_from_dataset_by_index(self):
        test_column_index = 2
        result = get_column_from_dataset_by_index(self.dataset, test_column_index)
        assert_equals(type(result), list)
        assert_equals(result[0], ('feature', self.dataset.transformed_header[test_column_index]))
        assert_equals(result[1], ('index', test_column_index))
        expected_column_data = [row[test_column_index] for row in self.dataset.transformed_rows]
        assert_equals(result[2], ('column', expected_column_data))

    def test_get_column_from_dataset_by_index_with_false(self):
        test_column_index = 2
        result = get_column_from_dataset_by_index(self.dataset, test_column_index, False)
        assert_equals(type(result), list)
        assert_equals(result[0], ('feature', self.dataset.header[test_column_index]))
        assert_equals(result[1], ('index', test_column_index))
        expected_column_data = [row[test_column_index] for row in self.dataset.rows]
        assert_equals(result[2], ('column', expected_column_data))

    def test_separate_data_from_class(self):
        result = separate_data_from_class(self.dataset)
        expected_data = [row[:len(row)-1] for row in self.dataset.transformed_rows]
        expected_targets = [row[len(row)-1] for row in self.dataset.transformed_rows]
        assert_equals(result[0], ('data', expected_data))
        assert_equals(result[1], ('targets', expected_targets))
