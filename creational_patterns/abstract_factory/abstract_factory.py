"""
Provides an interface for creating families of related or interdependent objects without specifying their specific
classes.
"""
from abc import ABCMeta, abstractmethod


class AbstractProductA(metaclass=ABCMeta):
    pass


class ProductA1(AbstractProductA):
    pass


class ProductA2(AbstractProductA):
    pass


class AbstractProductB(metaclass=ABCMeta):
    def interact(self, another_product: AbstractProductA) -> None:
        print('{} interacts with {}'.format(self.__class__.__name__, another_product.__class__.__name__))


class ProductB1(AbstractProductB):
    pass


class ProductB2(AbstractProductB):
    pass


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ProductB2()


factory1 = ConcreteFactory1()
product_a = factory1.create_product_a()
product_b = factory1.create_product_b()
product_b.interact(product_a)

factory2 = ConcreteFactory2()
product_a = factory2.create_product_a()
product_b = factory2.create_product_b()
product_b.interact(product_a)
