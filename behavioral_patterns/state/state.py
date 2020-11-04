"""
Allows an object to vary its behavior based on its internal state. From the outside, it looks like the class of the
object has changed.
"""
from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self):
        self.state = ConcreteStateA()

    def change_state(self, new_state):
        if new_state is True:
            self.state = ConcreteStateA()
        else:
            self.state = ConcreteStateB()

    def request(self):
        self.state.handle(self)


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, context):
        pass


class ConcreteStateA(State):
    def handle(self, context):
        print('Handle request with class \'{}\''.format(self.__class__.__name__))


class ConcreteStateB(State):
    def handle(self, context):
        print('Handle request with class \'{}\''.format(self.__class__.__name__))
        print('Change state from other state class.')
        context.change_state(True)


my_context = Context()
my_context.request()
my_context.change_state(False)
my_context.request()
my_context.request()
