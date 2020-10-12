"""
It is a surrogate for another object and controls access to it.
"""
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def action(self, x):
        pass


class RealSubject(Subject):
    def action(self, x):
        print(x)


class Proxy(Subject):
    def __init__(self):
        self.subject = None

    def action(self, x):
        if self.subject is None:
            self.subject = RealSubject()

        self.subject.action(x)


proxy = Proxy()
proxy.action('Hello')
