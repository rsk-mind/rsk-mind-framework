"""Errors.

This file contains all error classes defined
by RSKMind framework.
"""


class RSKMindError(Exception):
    """RSKMindError.

    The base class of the framework's errors.
    """

    def __init__(self, message=None):
        self.message = message or "General RSKMind framework error"

    def __str__(self):
        return self.message


class DatasourceReadError(RSKMindError):
    """DatasourceReadError.

    Error occurring while reading from a datasource.
    """

    def __init__(self, message=None):
        msg = message or "Error while reading from datasource"
        super(DatasourceReadError, self).__init__(msg)


class DatasourceWriteError(RSKMindError):
    """DatasourceWriteError.

    Error occurring while writing to a datasource.
    """

    def __init__(self, message=None):
        msg = message or "Error while writing to datasource"
        super(DatasourceWriteError, self).__init__(msg)


class ClassifierLoadModelError(RSKMindError):
    """ClassifierLoadModelError.

    Error occurring when loading a classifier's model.
    """

    def __init__(self, message=None):
        msg = message or "Error while loading classifier model"
        super(ClassifierLoadModelError, self).__init__(msg)


class ClassifierSaveModelError(RSKMindError):
    """ClassifierSaveModelError.

    Error occurring when saving a classifier's model.
    """

    def __init__(self, message=None):
        msg = message or "Error while saving classifier model"
        super(ClassifierSaveModelError, self).__init__(msg)


class InsufficientDatasetError(RSKMindError):
    """InsufficientDatasetError.

    Error occurring when dataset is very small.
    The case that makes sense is the training
    dataset.
    """

    def __init__(self, message=None):
        msg = message or "Dataset is not sufficient."
        super(InsufficientDatasetError, self).__init__(msg)


class UndefinedDatasetError(RSKMindError):
    """UndefinedDatasetError.

    Error occurring when dataset is None.
    """

    def __init__(self, message=None):
        msg = message or "Dataset is none."
        super(UndefinedDatasetError, self).__init__(msg)


class UndefinedClassifierModelError(RSKMindError):
    """UndefinedClassifierModelError.

    Error occurring when classifier's model is none.
    """

    def __init__(self, message=None):
        msg = message or "Model is none."
        super(UndefinedClassifierModelError, self).__init__(msg)
