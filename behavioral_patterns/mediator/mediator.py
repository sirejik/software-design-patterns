"""
Defines an object that encapsulates the way many objects interact. The mediator provides loose coupling of the system,
eliminating the need for objects to explicitly refer to each other and thus allowing them to independently change the
interactions between them.
"""
from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, message):
        pass


class Colleague(metaclass=ABCMeta):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator


class ConcreteMediator(Mediator):
    def __init__(self):
        self.receiver = None

    def set_receiver(self, colleague: Colleague):
        self.receiver = colleague

    def notify(self, message):
        self.receiver.receive(message)


class ConcreteColleague1(Colleague):
    def send(self, message):
        print('{} sent the message \'{}\'.'.format(self.__class__.__name__, message))
        self.mediator.notify(message)


class ConcreteColleague2(Colleague):
    def receive(self, message):
        print('{} received the message \'{}\'.'.format(self.__class__.__name__, message))


concrete_mediator = ConcreteMediator()

concrete_colleague1 = ConcreteColleague1(concrete_mediator)
concrete_colleague2 = ConcreteColleague2(concrete_mediator)

concrete_mediator.set_receiver(concrete_colleague2)

concrete_colleague1.send('Hello concrete_colleague2!')
