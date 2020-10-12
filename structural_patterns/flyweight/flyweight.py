"""
Uses partitioning to effectively support many small objects.
"""
from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def operation(self):
        pass


class FlyweightFactory:
    flyweights = {}

    @staticmethod
    def get_flyweight(name) -> Flyweight:
        return FlyweightFactory.flyweights.setdefault(name, ConcreteFlyweight(name))


class ConcreteFlyweight(Flyweight):
    def operation(self):
        print('Flyweight {} created'.format(self.name))


object_list = FlyweightFactory()
for i in range(10):
    object_list.get_flyweight('object_{}'.format(i % 3))

print(len(FlyweightFactory.flyweights))
