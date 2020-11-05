"""
Describes the operation performed on each object from some structure. The visitor pattern allows you to define a new
operation without changing the classes of these objects.
"""
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class ConcreteElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_element_a(self)

    @staticmethod
    def operation_a():
        print('operation_a')


class ConcreteElementB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_element_b(self)

    @staticmethod
    def operation_b():
        print('operation_b')


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit_concrete_element_a(self, element: ConcreteElementA):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element: ConcreteElementB):
        pass


class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element: ConcreteElementA):
        print(self.__class__.__name__)
        element.operation_a()

    def visit_concrete_element_b(self, element: ConcreteElementB):
        print(self.__class__.__name__)
        element.operation_b()


class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element: ConcreteElementA):
        print(self.__class__.__name__)
        element.operation_a()

    def visit_concrete_element_b(self, element: ConcreteElementB):
        print(self.__class__.__name__)
        element.operation_b()


element_a = ConcreteElementA()
element_b = ConcreteElementB()
visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()
element_a.accept(visitor1)
element_a.accept(visitor2)
element_b.accept(visitor1)
element_b.accept(visitor2)
