from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def operation(self):
        pass


class ConcreteA(Prototype):
    def operation(self):
        print('Hello {}!'.format(self.name))


class ConcreteB(Prototype):
    def operation(self):
        print('Goodbye {}!'.format(self.name))


concrete = ConcreteA('John')
concrete.operation()

concrete = ConcreteB('John')
concrete.operation()
