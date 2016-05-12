import os

from nose.tools import assert_equals, assert_items_equal
from rsk_mind.dataset import Dataset
from rsk_mind.transformer import *

class TestDataset:

    def setUp(self):
        self.header = ['a1', 'a2', 'y']
        self.rows = [['0', '0', '1'], ['0', '2', '1'], ['1', '0.5', '1'] ,['0.9', '2', '1']]

    def tearDown(self):
        # delete variables to release memory
        del self.header
        del self.rows

    def test_init(self):
        _dataset = Dataset(self.header, self.rows)

        assert_items_equal(_dataset.header, self.header)
        assert_items_equal(_dataset.rows, self.rows)
        assert_items_equal(_dataset.transformed_rows, [])
        assert_equals(_dataset.transformer, None)
        assert_equals(_dataset.transformed_header, None)

    def test_setTransformer(self):
        _dataset = Dataset(self.header, self.rows)
        _transformer = Transformer()
        _dataset.setTransformer(_transformer)

        assert_equals(_dataset.transformer, _transformer)

    def test_applyTransformations(self):
        pass

    def test_applyRowTransformation(self):
        pass
