"""
Provides a unified interface instead of a set of interfaces for some subsystem. The facade defines a higher-level
interface that makes the subsystem easier to use.
"""


class FooClass:
    @staticmethod
    def foo1():
        print('foo1')

    @staticmethod
    def foo2():
        print('foo2')


class BarClass:
    @staticmethod
    def bar1():
        print('bar1')

    @staticmethod
    def bar2():
        print('bar2')


class Facade:
    def __init__(self):
        self.foo_class = FooClass()
        self.bar_class = BarClass()

    def foo(self):
        self.foo_class.foo1()
        self.foo_class.foo2()
        self.bar_class.bar1()


facade = Facade()
facade.foo()
