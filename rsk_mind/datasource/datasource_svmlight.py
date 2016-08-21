from datasource import DataSource
from ..dataset import Dataset
import os


class SVMLightDataSource(DataSource):
    """Handle SVMLight formatted datasource.

    All the methods to handle a SVMLight formatted datasource.

    """

    def __init__(self, path):
        """Create a new SVMLight Datasource.

        :param path: a path to SVMLight file.
        """
        super(SVMLightDataSource, self).__init__(path)

    def read(self):
        """Read SVMLight formatted datasource from specified path.

        Read datasource and load it on memory.

        :return: SVMLight
        """
        # NOTE: svmlight format does not include
        # names for features, it only uses indexes.
        # So headers will be auto-generated from
        # indexes.
        header = []
        rows = []
        with open(self.path, "r+b") as infile:
            lines = infile.readlines()
            # iterate over lines
            for line in lines:
                # strip new line
                line = line.rstrip('\n')
                # split on " "
                tokens = line.split(" ")
                # first token is the target(y/n , 1/0)
                target = float(tokens[0])
                # get last token (it's form is indexN:value)
                # and determine the length of features
                last_index = tokens[len(tokens) - 1].split(":")[0]
                # length of features is last_index+1 (zero based)
                # create a list of zeroes
                row = [0.0] * (int(last_index) + 1)
                # set value to row index according to current row
                for i in range(1, len(tokens)):
                    parts = tokens[i].split(":")
                    feat_index = int(parts[0])
                    feat_value = float(parts[1])
                    row[feat_index] = feat_value
                # append target to the end of row
                row.append(target)
                # append row vector to rows
                rows.append(row)
        # create header
        for i in range(0, len(rows[0]) - 1):
            header.append("f_" + str(i))
        header.append("target")

        return Dataset(header, rows)

    def write(self, dataset, write_transformed=True):
        """Save SVMLight formatted dataset on disk.

        :param dataset:
        :param write_transformed:
        """
        # NOTE consider the last feature as the Target
        # Get the size of features excluding the last one
        # because it's the target.
        features_with_target = len(dataset.transformed_header)
        features_without_target = features_with_target - 1
        # open file to write
        with open(self.path, "w+b") as outfile:
            # iterate over row
            for row in dataset.transformed_rows:
                # create a string for the row
                row_str = ""
                # iterate over features
                for i in range(0, features_without_target):
                    if row[i] != 0.0:
                        row_str += "{}:{} ".format(i, row[i])
                # append target value to the beginning and rstrip
                target_value = row[features_without_target]
                row_str = ("{} ".format(target_value) + row_str).rstrip(" ")
                # write row_str to file
                outfile.write(row_str)
                outfile.write(os.linesep)
