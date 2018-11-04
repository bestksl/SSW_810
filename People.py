import abc


class People(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        pass

    @abc.abstractmethod
    def pt_show(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def get_fields():
        pass
