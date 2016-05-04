class Dataset():
    """ """

    def __init__(self, header, rows):
        """ """
        self.header = header
        self.rows = rows
        self.transformer = None
        self.transformed_rows = []
        self.transformed_header = []

    def setTransformer(self, transformer):
        """ """
        self.transformer = transformer

    def applyTransformations(self):
        """ """
        self.transformed_header = self.header
        for row in self.rows:
            self.applyRowTransformation(row)

    def applyRowTransformation(self, row):
        """ """
        if self.transformer == None:
            transformed_row = row

        else:
            transformed_row = []
            for cell in row:
                transformed_row += [float(cell) / 1000]

        self.transformed_rows += [transformed_row]
