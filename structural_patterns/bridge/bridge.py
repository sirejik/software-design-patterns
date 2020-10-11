"""
Separate the abstraction from its implementation so that both can be changed independently.
"""
from abc import ABCMeta, abstractmethod


class Implementor(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation_impl(self):
        pass


class ConcreteImplementationA(Implementor):
    def operation_impl(self):
        print('ConcreteImplementationA operation.')


class ConcreteImplementationB(Implementor):
    def operation_impl(self):
        print('ConcreteImplementationB operation.')


class Abstraction(metaclass=ABCMeta):
    def __init__(self, implementor: Implementor):
        self.implementor = implementor

    @abstractmethod
    def operation(self):
        pass


class RefinedAbstraction(Abstraction):
    def __init__(self, implementor: Implementor):
        super(RefinedAbstraction, self).__init__(implementor)

    def operation(self):
        print('RefinedAbstraction operation')
        return self.implementor.operation_impl()


refined_abstractions = [RefinedAbstraction(ConcreteImplementationA()), RefinedAbstraction(ConcreteImplementationB())]
[x.operation() for x in refined_abstractions]
