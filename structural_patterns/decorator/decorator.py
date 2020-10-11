"""
Dynamically adds new responsibilities to the object. Provides a flexible alternative to subclassing to extend
functionality.
"""
from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print('ConcreteComponent')


class Decorator(Component):
    def __init__(self, component: Component):
        self.component = component

    def operation(self):
        print('Decorator')
        self.component.operation()


concrete_component = ConcreteComponent()
concrete_component = Decorator(concrete_component)
concrete_component.operation()
