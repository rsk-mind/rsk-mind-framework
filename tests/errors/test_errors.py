from nose.tools import assert_equal

from rsk_mind.errors import *
from rsk_mind.errors.errors import RSKMindError


class TestRSKMindError:
    def setUp(self):
        self._test_message = "Very bad error!"

    def test_empty(self):
        _error = RSKMindError()
        _expected_message = "General RSKMind framework error"
        assert_equal(str(_error), _expected_message)
        assert_equal(_error.message, _expected_message)

    def test_message(self):
        _error = RSKMindError(self._test_message)
        assert_equal(str(_error), self._test_message)
        assert_equal(_error.message, self._test_message)


class TestDatasourceReadError:
    def setUp(self):
        self._test_message = "Very bad error!"

    def test_empty(self):
        _error = DatasourceReadError()
        _expected_message = "Error while reading from datasource"
        assert_equal(_error.message, _expected_message)

    def test_message(self):
        _error = DatasourceReadError(self._test_message)
        assert_equal(_error.message, self._test_message)


class TestDatasourceWriteError:
    def setUp(self):
        self._test_message = "Very bad error!"

    def test_empty(self):
        _error = DatasourceWriteError()
        _expected_message = "Error while writing to datasource"
        assert_equal(_error.message, _expected_message)

    def test_message(self):
        _error = DatasourceWriteError(self._test_message)
        assert_equal(_error.message, self._test_message)


class TestClassifierLoadModelError:
    def setUp(self):
        self._test_message = "Very bad error!"

    def test_empty(self):
        _error = ClassifierLoadModelError()
        _expected_message = "Error while loading classifier model"
        assert_equal(_error.message, _expected_message)

    def test_message(self):
        _error = ClassifierLoadModelError(self._test_message)
        assert_equal(_error.message, self._test_message)


class TestClassifierSaveModelError:
    def setUp(self):
        self._test_message = "Very bad error!"

    def test_empty(self):
        _error = ClassifierSaveModelError()
        _expected_message = "Error while saving classifier model"
        assert_equal(_error.message, _expected_message)

    def test_message(self):
        _error = ClassifierSaveModelError(self._test_message)
        assert_equal(_error.message, self._test_message)


class TestInsufficientDatasetError:
    def setUp(self):
        self._test_message = "Very bad error!"

    def test_empty(self):
        _error = InsufficientDatasetError()
        _expected_message = "Dataset is not sufficient."
        assert_equal(_error.message, _expected_message)

    def test_message(self):
        _error = InsufficientDatasetError(self._test_message)
        assert_equal(_error.message, self._test_message)


class TestUndefinedDatasetError:
    def setUp(self):
        self._test_message = "Very bad error!"

    def test_empty(self):
        _error = UndefinedDatasetError()
        _expected_message = "Dataset is none."
        assert_equal(_error.message, _expected_message)

    def test_message(self):
        _error = UndefinedDatasetError(self._test_message)
        assert_equal(_error.message, self._test_message)


class TestUndefinedClassifierModelError:
    def setUp(self):
        self._test_message = "Very bad error!"

    def test_empty(self):
        _error = UndefinedClassifierModelError()
        _expected_message = "Model is none."
        assert_equal(_error.message, _expected_message)

    def test_message(self):
        _error = UndefinedClassifierModelError(self._test_message)
        assert_equal(_error.message, self._test_message)
