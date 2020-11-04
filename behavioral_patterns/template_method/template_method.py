"""
The template method defines the basis of the algorithm and allows subclasses to override some steps of the algorithm
without changing its structure as a whole.
"""
from abc import abstractmethod


class AbstractClass:
    def template_method(self):
        self.primitive_operation1()
        self.primitive_operation2()

    @abstractmethod
    def primitive_operation1(self):
        pass

    @abstractmethod
    def primitive_operation2(self):
        pass


class ConcreteClass(AbstractClass):
    def primitive_operation1(self):
        print('Execute \'primitive_operation1\' method.')

    def primitive_operation2(self):
        print('Execute \'primitive_operation2\' method.')


concrete_class = ConcreteClass()
concrete_class.template_method()
