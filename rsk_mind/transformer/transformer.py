class Transformer(object):

    class Feats():
        exclude = None
        pass

    def __init__(self):
        for field in self.get_feats():
            getattr(self.Feats, field).bind(field, self)

    def get_feats(self):
        return [x for x in dir(self.Feats) if not (x.startswith('__') or x in ['exclude'] )]

    def default(self, feat):
        return [feat]
