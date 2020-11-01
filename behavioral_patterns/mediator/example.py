import inspect

from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def send(self, message):
        pass


class Colleague(metaclass=ABCMeta):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass


class SkypeMediator(Mediator):
    def __init__(self):
        self.first = None
        self.second = None

    def set_first(self, colleague: Colleague):
        self.first = colleague

    def set_second(self, colleague: Colleague):
        self.second = colleague

    def send(self, message):
        sender = inspect.currentframe().f_back.f_locals['self']
        receiver = self.first if sender == self.second else self.second
        receiver.receive(message)


class Alice(Colleague):
    def send(self, message):
        print('{} sent the message \'{}\'.'.format(self.__class__.__name__, message))
        self.mediator.send(message)

    def receive(self, message):
        print('{} receive the message \'{}\'.'.format(self.__class__.__name__, message))


class Bob(Colleague):
    def send(self, message):
        print('{} sent the message \'{}\'.'.format(self.__class__.__name__, message))
        self.mediator.send(message)

    def receive(self, message):
        print('{} receive the message \'{}\'.'.format(self.__class__.__name__, message))


concrete_mediator = SkypeMediator()

alice = Alice(concrete_mediator)
bob = Bob(concrete_mediator)

concrete_mediator.set_first(alice)
concrete_mediator.set_second(bob)

alice.send('Hello Bob!')
bob.send('Hello Alice!')
