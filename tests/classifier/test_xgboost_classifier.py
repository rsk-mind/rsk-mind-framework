from nose.tools import (
    assert_equals,
    assert_not_equals,
    assert_true
)
from random import randint
import os
from rsk_mind.classifier import XgboostClassifier
from rsk_mind.dataset import (
    Splitter,
    Dataset
)


class TestXgboostClassifier(object):

    @classmethod
    def setup_class(cls):
        cls.nr_columns = 11
        cls.nr_rows = 100

        header = []
        for i in range(cls.nr_columns-1):
            header.append("f_{}".format(i))
        header.append("target")
        rows = []
        for row_idx in range(cls.nr_rows):
            row = []
            for col_idx in range(cls.nr_columns):
                row.append(randint(0, 1))
            rows.append(row)

        cls.original_dataset = Dataset(header, rows)
        cls.original_dataset.transformed_header = list(header)
        cls.original_dataset.transformed_rows = list(rows)

        _splitter = Splitter(cls.original_dataset)
        cls.training_dataset = _splitter.training_dataset
        cls.validation_dataset = _splitter.validation_dataset
        cls.test_dataset = _splitter.test_dataset

        cls.model_path = os.path.join(os.getcwd(),'xgb_model.bin')

        cls.test_classifier = XgboostClassifier()

    @classmethod
    def teardown_class(cls):
        del cls.training_dataset
        del cls.validation_dataset
        del cls.test_dataset
        del cls.original_dataset
        if os.path.exists(cls.model_path):
            os.remove(cls.model_path)
        del cls.model_path
        del cls.test_classifier

    def test_01_empty_training_dataset_of_classifier(self):
        assert_equals(self.test_classifier.training_dataset, None)

    def test_02_set_training_dataset_to_classifier(self):
        self.test_classifier.training_dataset = self.training_dataset
        assert_not_equals(self.test_classifier.training_dataset, None)

    def test_03_empty_validation_dataset_of_classifier(self):
        assert_equals(self.test_classifier.validation_dataset, None)

    def test_04_set_validation_dataset_to_classifier(self):
        self.test_classifier.validation_dataset = self.validation_dataset
        assert_not_equals(self.test_classifier.validation_dataset, None)

    def test_05_empty_test_dataset_of_classifier(self):
        assert_equals(self.test_classifier.test_dataset, None)

    def test_06_set_test_dataset_to_classifier(self):
        self.test_classifier.test_dataset = self.test_dataset
        assert_not_equals(self.test_classifier.test_dataset, None)

    def test_07_train(self):
        self.test_classifier.train()
        assert_not_equals(self.test_classifier.model, None)

    def test_08_save_model(self):
        self.test_classifier.save_model(self.model_path)
        save_operation = os.path.exists(self.model_path) and os.path.isfile(self.model_path)
        assert_equals(save_operation, True)

    def test_09_evaluate(self):
        summary = self.test_classifier.evaluate(0.05)
        assert_not_equals(summary, None)

    def test_10_predict(self):
        instance = []
        for i in range(self.nr_columns):
            instance.append(randint(0, 1))
        score = self.test_classifier.predict(instance)
        assert_true(score >= 0 and score <= 1)

    def test_11_load_model(self):
        self.test_classifier.model = None
        assert_equals(self.test_classifier.model, None)
        self.test_classifier.load_model(self.model_path)
        assert_not_equals(self.test_classifier.model, None)

