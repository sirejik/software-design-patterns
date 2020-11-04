from abc import ABCMeta, abstractmethod


class Navigator:
    def __init__(self, strategy):
        self.strategy = strategy

    def find_route(self):
        self.strategy.find_route()

    def change_strategy(self, strategy):
        self.strategy = strategy


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def find_route(self):
        pass


class FootStrategy(Strategy):
    def find_route(self):
        print('The walking route was built.')


class CarStrategy(Strategy):
    def find_route(self):
        print('The car route was built.')


context = Navigator(FootStrategy())
context.find_route()
context.change_strategy(CarStrategy())
context.find_route()
