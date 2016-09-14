"""Utils.

This file provides functions as utilities.
It makes sense if something can be written
in one method rather than creating a class
then this is the file one can add his/her
method.
"""

def separate_data_from_class(dataset):
    """Separate features from classes.

    This method separates feature vectors
    from their classes. This separation might
    be useful for some classifiers.
    Note that RSKMind framework considers
    target to be the last element in a row.

    :param dataset: given dataset to process
    :type dataset: Dataset
    """
    data = []
    targets = []
    rows = list(dataset.transformed_rows)

    for row in rows:
        features = row[:len(row)-1]
        target = row[len(row)-1]
        data.append(features)
        targets.append(target)

    return [('data', data), ('targets', targets)]

def get_column_from_dataset_by_index(dataset, column_index, from_tranformed=True):
    """Get a column from dataset.

    :param dataset: given dataset
    :type dataset: Dataset
    :param column_index: index of dataset's column
    :type column_index: int
    :param from_transformed: indicates if the column should be taken from transformed_rows
    :param from_transformed: bool
    """
    if from_tranformed:
        header = dataset.transformed_header
        rows = dataset.transformed_rows
    else:
        header = dataset.header
        rows = dataset.rows

    if column_index >=0 and column_index < len(header):
        feature_name = header[column_index]
        column = []
        for row in rows:
            column.append(row[column_index])
    else:
        raise IndexError("Invalid column index {}".format(column_index))

    return [('feature', feature_name), ('index', column_index), ('column', column)]

def strings_to_numeric(strings_list):
    """Convert strings to numbers.

    This method will try to convert
    a list of strings such as
    ['1', '0.0', '0', '1.0'] to its
    respective list of numerical values
    [1, 0, 0, 1]

    :param strings_list: a list of strings
    :type strings_list: list
    """
    converted = []
    for s in strings_list:
        try:
            num = int(float(s))
            converted.append(num)
        except ValueError as ve:
            raise ve

    return [('converted', converted)]
