from datasource import Datasource
from ..dataset import Dataset
from numbers import Number


class ArffDatasource(Datasource):

  def __init__(self, path):
    super(ArffDatasource, self).__init__(path)

  def read(self):
    header = []
    rows = []

    lines = []
    with open(self.path, "r+b") as infile:
      temp = infile.readlines()
      lines = map(lambda x: x.lower(), temp)
      del temp

    useless_lines = filter(
        lambda l: (l.startswith('%') or l.startswith('@relation') or
                   l.startswith('@data') or len(l) == 0 or l == '\n'),
        lines)

    useful_lines = [x for x in lines if x not in useless_lines]

    del useless_lines
    del lines

    # now we can iterate through useful lines
    for line in useful_lines:
      line = line.rstrip('\n')
      if line.startswith('@attribute'):
        header.append(line.split(" ")[1])
      else:
        row_data = line.rstrip("\n").split(",")
        row = []
        for value in row_data:
          try:
            row.append(float(value))
          except ValueError:
            rows.append(value)
        rows.append(row)

    return Dataset(header, rows)

  def write(self, dataset):
    transformed_header = dataset.transformed_header
    transformed_rows = dataset.transformed_rows
    if (not transformed_header) or (not transformed_rows):
      raise Exception("Transformed header and transformed rows must not be empty")
    sample = transformed_rows[0]

    # open file for writing
    with open(self.path, "w+b") as outfile:

      outfile.write("@RELATION OUTPUT_RELATION\n")
      for idx, th in enumerate(transformed_header):
        feature_type = "NUMERIC" if isinstance(sample[idx], Number) else "STRING"
        attr_line = "{} {} {}\n".format("@ATTRIBUTE", th, feature_type)
        outfile.write(attr_line)
      outfile.write("@DATA\n")
      for tr in transformed_rows:
        data_line = ",".join(str(x) for x in tr)
        outfile.write(data_line)
