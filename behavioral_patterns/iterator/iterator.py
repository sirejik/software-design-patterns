"""
Provides a way to sequentially access all the elements of a composite object without exposing its internal
representation.
"""
from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._cursor = 0

    def current(self):
        if self._cursor < len(self._collection):
            return self._collection[self._cursor]

        self._raise_error(self._cursor)

    def next(self):
        if len(self._collection) > self._cursor + 1:
            self._cursor += 1
            return self._collection[self._cursor]

        self._raise_error(self._cursor)

    def has_next(self):
        return len(self._collection) > self._cursor + 1

    def _raise_error(self, key):
        raise IndexError('Collection does not have key \'{}\'.'.format(key))


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def create_iterator(self):
        pass


class ConcreteAggregate(Aggregate):
    def __init__(self, collection):
        self._collection = collection

    def create_iterator(self):
        return ConcreteIterator(self._collection)


class Client:
    @staticmethod
    def foo():
        collection = ConcreteAggregate([1, 2, 3, 4, 5])
        iterator = collection.create_iterator()
        print(iterator.current())
        while iterator.has_next():
            print(iterator.next())


client = Client()
client.foo()
