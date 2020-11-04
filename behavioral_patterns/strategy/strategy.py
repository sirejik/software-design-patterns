"""
Defines a family of algorithms, encapsulates each of them and makes them interchangeable. The strategy allows algorithms
to be changed independently of the clients who use them.
"""
from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()

    def change_strategy(self, strategy):
        self.strategy = strategy


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self):
        print('Execute strategy \'{}\'.'.format(self.__class__.__name__))


class ConcreteStrategyB(Strategy):
    def execute(self):
        print('Execute strategy \'{}\'.'.format(self.__class__.__name__))


context = Context(ConcreteStrategyA())
context.execute_strategy()
context.change_strategy(ConcreteStrategyB())
context.execute_strategy()
