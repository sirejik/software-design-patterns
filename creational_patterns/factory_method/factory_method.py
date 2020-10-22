"""
Defines the interface for creating an object, but leaves the subclasses to decide which class to instantiate.
"""
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print(self):
        pass


class ConcreteProduct(Product):
    def print(self):
        print('Concrete {}'.format(self.name))


class Creator(metaclass=ABCMeta):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def operation(self):
        product = self.factory_method()
        product.print()


class ConcreteCreator(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct('product')


concrete_creator = ConcreteCreator()
concrete_creator.operation()
