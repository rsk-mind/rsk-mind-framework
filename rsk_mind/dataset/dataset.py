class Dataset():
    """ """

    def __init__(self, header, rows):
        """ """
        self.header = header
        self.rows = rows
        self.transformer = None
        self.trn = {}
        self.transformed_rows = []
        self.transformed_header = []

    def setTransformer(self, transformer):
        """ """
        self.transformer = transformer
        self.trn = self.transformer.__dict__

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
            for i, cell in enumerate(row):
                feat = self.header[i]
                if feat in self.trn:
                    mytrans = self.trn[feat]
                else:
                    mytrans = self.transformer.default

                transformed_row += mytrans(cell)

        self.transformed_rows += [transformed_row]
