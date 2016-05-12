class Feat(object):

    def __init__(self):
        self.field_name = None
        self.parent = None

    def bind(self, field_name, parent):
        self.field_name = field_name
        self.parent = parent

    def transform(self, x):
        fun = getattr(self.parent, 'get_%s' % self.field_name)
        return fun(x)

class CompositeFeat(Feat):

    def __init__(self, attrs):
        super(CompositeFeat, self).__init__()
        self.attrs = attrs

    def transform(self, header, row):
        args = []
        for attr in self.attrs:
            args.append(row[header.index(attr)])

        fun = getattr(self.parent, 'get_%s' % self.field_name)
        return fun(*args)
