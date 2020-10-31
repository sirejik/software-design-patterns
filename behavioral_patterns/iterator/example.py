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


class TreeIterator(Iterator):
    def __init__(self, collection):
        self._generator = self._get_next_value(collection)
        self._current = None
        self._is_last = None

    def current(self):
        if self._current is None:
            self.get_next()

        return self._current

    def next(self):
        self.get_next()
        return self._current

    def has_next(self):
        if self._is_last is None:
            self.get_next()

        return not self._is_last

    def get_next(self):
        self._current, self._is_last = self._generator.__next__()

    def _get_next_value(self, branch, previous=True):
        for i in range(0, len(branch)):
            elem = branch[i]
            is_last = (i == len(branch) - 1) and previous
            if isinstance(elem, list):
                yield from self._get_next_value(elem, is_last)
            else:
                yield elem, is_last


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def create_iterator(self):
        pass


class TreeAggregate(Aggregate):
    def __init__(self, collection):
        self._collection = collection

    def create_iterator(self):
        return TreeIterator(self._collection)


class Client:
    @staticmethod
    def foo():
        collection = TreeAggregate([1, [2, [3], 4], 5, [6, [7, 8]], 9])
        iterator = collection.create_iterator()
        print(iterator.current())
        while iterator.has_next():
            print(iterator.next())


client = Client()
client.foo()
