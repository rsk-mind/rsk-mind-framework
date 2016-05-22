import os

from nose.tools import assert_equals, assert_items_equal

from rsk_mind.dataset import PandasDataset
from rsk_mind.transformer import *

import pandas as pd


class CustomTransformer(Transformer):
    class Feats():
        a1 = Feat()
        a2 = Feat()

        f1 = CompositeFeat(['a1', 'a2'])

    def get_a1(self, feat):
        return [-float(feat), 'fa']

    def get_a2(self, feat):
        return [-float(feat)]

    def get_f1(self, a1, a2):
        return [float(a1) + float(a2)]


class TestPandasDataset:

    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'tests/files/in.csv')
        self.reader = pd.read_table(self.path, sep=',', chunksize=1000)

    def tearDown(self):
        # delete variables to release memory
        del self.path
        del self.reader

    def test_init(self):
        _dataset = PandasDataset(self.reader)

        assert_equals(_dataset.reader, self.reader)
        assert_equals(_dataset.header, None)
        assert_equals(_dataset.rows, None)
        assert_items_equal(_dataset.transformed_rows, [])
        assert_equals(_dataset.transformer, None)
        assert_equals(_dataset.transformed_header, None)

    def test_setTransformer(self):
        _dataset = PandasDataset(self.reader)
        _transformer = CustomTransformer()
        _dataset.setTransformer(_transformer)

        assert_equals(_dataset.transformer, _transformer)

    def test_applyTransformations(self):
        _dataset = PandasDataset(self.reader)
        _transformer = CustomTransformer()
        _dataset.setTransformer(_transformer)

        _header = ['a1_0', 'a1_1', 'a2', 'f1', 'a3', 'a4', 'target']
        _rows = [[-0.0, 'fa',  -0.0, 0.0, 0, 0, 1], [-1.0, 'fa', -1.0, 2.0, 0, 1, 0], [-1.0, 'fa', -0.0, 1.0, 0, 1, 0]]

        _dataset.applyTransformations()

        assert_equals(_dataset.transformed_header, _header)
        assert_items_equal(_dataset.transformed_rows, _rows)
        assert_equals(_dataset.transformer, _transformer)

    def test_applyTransformations_Without_Transformer(self):
        _dataset = PandasDataset(self.reader)

        _expected_header = ['a1', 'a2', 'a3', 'a4', 'target']
        _expected_rows = [[0, 0, 0, 0, 1], [1, 1, 0, 1, 0], [1, 0, 0, 1, 0]]

        _dataset.applyTransformations()

        assert_equals(_dataset.transformed_header, _expected_header)
        assert_items_equal(_dataset.transformed_rows, _expected_rows)
        assert_equals(_dataset.transformer, None)
