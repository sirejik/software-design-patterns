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
        self.state.handle()


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    def handle(self):
        print('Handle request with class \'{}\''.format(self.__class__.__name__))


class ConcreteStateB(State):
    def handle(self):
        print('Handle request with class \'{}\''.format(self.__class__.__name__))


context = Context()
context.request()
context.change_state(False)
context.request()
