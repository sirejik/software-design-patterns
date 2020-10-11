from abc import ABCMeta, abstractmethod


class Product:
    def __init__(self):
        self.param1 = None
        self.param2 = None

    def set_param1(self, param):
        self.param1 = param

    def set_param2(self, param):
        self.param2 = param

    def __repr__(self):
        return "Product with the following parameters: parameter1 '{}' and parameter2 '{}'.".format(
            self.param1, self.param2
        )


class Builder(metaclass=ABCMeta):
    def __init__(self):
        self.product = Product()

    @abstractmethod
    def build1(self):
        pass

    @abstractmethod
    def build2(self):
        pass

    def get_product(self):
        return self.product


class ConcreteBuilder(Builder):
    def build1(self):
        self.product.set_param1("first")

    def build2(self):
        self.product.set_param2("second")


class Director(metaclass=ABCMeta):
    def __init__(self, builder: Builder):
        self.builder = builder

    def build(self):
        self.builder.build1()
        self.builder.build2()

    def get_product(self):
        return self.builder.get_product()


concrete_builder = ConcreteBuilder()
director = Director(concrete_builder)
director.build()
product = director.get_product()
print(product)
