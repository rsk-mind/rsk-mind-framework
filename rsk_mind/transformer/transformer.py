class Transformer(object):

    class Fields():
        exclude = None
        pass

    def __init__(self):
        for field in self.get_fields():
            getattr(self.Fields, field).bind(field, self)

    def get_fields(self):
        return [x for x in dir(self.Fields) if not (x.startswith('__') or x in ['exclude'] )]

    def default(self, feat):
        return [feat]
