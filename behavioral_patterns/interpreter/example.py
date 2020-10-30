from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    def __init__(self):
        self.vars = {}

    def get_var(self, name):
        return self.vars[name]

    def set_var(self, name, value):
        self.vars[name] = value


class AbstractExpression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, context: Context):
        pass


class ConstExpression(AbstractExpression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context: Context):
        return self.value


class VarExpression(AbstractExpression):
    def __init__(self, var_name):
        self.var_name = var_name

    def interpret(self, context: Context):
        return context.get_var(self.var_name)


class AdditionExpression(AbstractExpression):
    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right

    def interpret(self, context: Context):
        return self.left.interpret(context) + self.right.interpret(context)


class SubtractionExpression(AbstractExpression):
    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right

    def interpret(self, context: Context):
        return self.left.interpret(context) - self.right.interpret(context)


class MultiplicationExpression(AbstractExpression):
    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right

    def interpret(self, context: Context):
        return self.left.interpret(context) * self.right.interpret(context)


class DivisionExpression(AbstractExpression):
    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right

    def interpret(self, context: Context):
        return self.left.interpret(context) / self.right.interpret(context)


contexts = Context()
contexts.set_var('x', 5)
contexts.set_var('y', 10)
expressions = AdditionExpression(
    SubtractionExpression(
        VarExpression('x'),
        ConstExpression(1)
    ),
    MultiplicationExpression(
        DivisionExpression(
            VarExpression('y'),
            VarExpression('y')
        ),
        ConstExpression(2)
    )
)
result = expressions.interpret(contexts)
print(result)
