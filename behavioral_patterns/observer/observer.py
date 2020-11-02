"""
Defines a one-to-many dependency between objects in such a way that when the state of one object changes, everyone who
depends on it is notified and automatically updated.
"""
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, message):
        pass


class ConcreteObserver(Observer):
    def update(self, message):
        print('{} received the message: {}'.format(self, message))


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


concrete_subject = ConcreteSubject()
concrete_subject.attach(ConcreteObserver())
concrete_subject.attach(ConcreteObserver())
concrete_subject.notify('Hello world!')
