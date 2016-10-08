from abc import ABCMeta, abstractmethod


class Engine(object):
    __metaclass__ = ABCMeta

    def initialize(self):
        """Initialize a Engine
        """
        self.build()
        self.start()

    @abstractmethod
    def start(self):
        """Start REST API for new data mining service
        """
        pass

    @abstractmethod
    def build(self, rebuild=False):
        """Build new model from dataset.

        if rebuild flag is True overrides previous model.
        :return: a data mining model.
        """
        pass

    def rebuild(self):
        """Rebuild model

        :return: a data mining model.
        """
        return self.build(True)
