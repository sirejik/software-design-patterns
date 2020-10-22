"""
Specifies the types of objects to create using a prototype instance and creates new objects by copying this prototype.
"""
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass


class Concrete(Prototype):
    def operation(self):
        print("Hello world!")


concrete = Concrete()
concrete.operation()
