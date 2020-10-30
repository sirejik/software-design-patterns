"""
For a given language, determines the representation of its grammar, as well as the interpreter of the sentences of this
language.
"""
from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class AbstractExpression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, context: Context):
        pass


class TerminalExpression(AbstractExpression):
    def interpret(self, context: Context):
        print("TerminalExpression")
        print(context.get_value())


class NonTerminalExpression(AbstractExpression):
    def __init__(self, expression: AbstractExpression):
        self.expression = expression

    def interpret(self, context: Context):
        print("NonTerminalExpression")
        self.expression.interpret(context)


hello_context = Context(value='Hello')
expressions = NonTerminalExpression(
    TerminalExpression()
)
expressions.interpret(hello_context)
