"""
Separates the construction of a complex object from its representation, so that different representations can result
from the same design process.
"""
from abc import ABCMeta, abstractmethod


class Product:
    def __init__(self):
        self.param = None

    def set_param(self, param):
        self.param = param

    def __repr__(self):
        return 'Product with the following parameters: parameter \'{}\'.'.format(self.param)


class Builder(metaclass=ABCMeta):
    def __init__(self):
        self.product = Product()

    @abstractmethod
    def build(self):
        pass

    def get_product(self):
        return self.product


class ConcreteBuilder(Builder):
    def build(self):
        self.product.set_param('param')


class Director(metaclass=ABCMeta):
    def __init__(self, builder: Builder):
        self.builder = builder

    def build(self):
        self.builder.build()

    def get_product(self):
        return self.builder.get_product()


concrete_builder = ConcreteBuilder()
director = Director(concrete_builder)
director.build()
product = director.get_product()
print(product)
