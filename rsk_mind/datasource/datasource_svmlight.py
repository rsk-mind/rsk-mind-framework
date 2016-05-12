from datasource import Datasource
from ..dataset import Dataset
import os


class SVMLightDatasource(Datasource):

    def __init__(self, path):
        super(SVMLightDatasource, self).__init__(path)

    def read(self):
        # NOTE: svmlight format does not include
        # names for features, it only uses indexes.
        # So headers will be auto-genenerated from
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

    def write(self, dataset):
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
                # append target value to the begining and rstrip
                target_value = row[features_without_target]
                row_str = ("{} ".format(target_value) + row_str).rstrip(" ")
                # write row_str to file
                outfile.write(row_str)
                outfile.write(os.linesep)
