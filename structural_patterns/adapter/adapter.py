"""
Converts the interface of one class to the interface of another that clients expect. The adapter allows classes with
incompatible interfaces to work together that would not be possible without it.
"""
from abc import ABCMeta, abstractmethod


class Adaptee1:
    def foo1(self):
        print('Function {} called from {} class.'.format(self.foo1.__name__, self.__class__.__name__))


class Adaptee2:
    def foo2(self):
        print('Function {} called from {} class.'.format(self.foo2.__name__, self.__class__.__name__))


class AbstractAdapter(metaclass=ABCMeta):
    @abstractmethod
    def request(self):
        pass


class Adapter1(AbstractAdapter, Adaptee1):
    def request(self):
        self.foo1()


class Adapter2(AbstractAdapter, Adaptee2):
    def request(self):
        self.foo2()


class Target:
    def __init__(self, adapter: AbstractAdapter):
        self.adapter = adapter

    def call_request(self):
        self.adapter.request()


client = Target(Adapter1())
client.call_request()

client = Target(Adapter2())
client.call_request()
