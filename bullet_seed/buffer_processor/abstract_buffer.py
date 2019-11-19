from abc import ABCMeta, abstractmethod


class AbstractBuffer(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_capacity(self):
        pass

    @abstractmethod
    def get_length(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def insert(self, record):
        pass

    @abstractmethod
    def flush(self):
        pass
