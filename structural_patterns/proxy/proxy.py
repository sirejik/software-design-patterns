from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def foo(self, x):
        pass

    @abstractmethod
    def bar(self, x):
        pass


class RealSubject(Subject):
    def foo(self, x):
        print(x)

    def bar(self, x):
        print('\t{}'.format(x))


class Proxy(Subject):
    def __init__(self):
        self.subject = None

    def foo(self, x):
        if self.subject is None:
            self.subject = RealSubject()

        self.subject.foo(x)

    def bar(self, x):
        if self.subject is None:
            self.subject = RealSubject()

        self.subject.bar(x)


proxy = Proxy()
proxy.foo('Hello')
proxy.bar('world')
