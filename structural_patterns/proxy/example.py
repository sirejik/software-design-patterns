import time

from abc import ABCMeta, abstractmethod


class DataReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self, position):
        pass


class HTTPReader(DataReader):
    def __init__(self):
        print('Long HTTPReader initialization.')
        time.sleep(5)
        print('Initialization completed.')

    def read(self, position):
        print('Read data from {}.'.format(position))


class Proxy(DataReader):
    def __init__(self):
        self.subject = None

    def read(self, position):
        if self.subject is None:
            self.subject = HTTPReader()

        self.subject.read(position)


print('Initializing Proxy...')
proxy = Proxy()
print('Reading data...')
proxy.read(10)
