from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def operation(self, n):
        pass


class Leaf(Component):
    def operation(self, n):
        print('\t' * n + 'Leaf "{}"'.format(self.name))


class Composite(Component):
    def __init__(self, name):
        super(Composite, self).__init__(name)
        self.children = []

    def add(self, leaf: Component):
        self.children.append(leaf)

    def operation(self, n=0):
        print('\t' * n + 'Branch "{}"'.format(self.name))
        for child in self.children:
            child.operation(n + 1)


root = Composite('root')
root.add(Leaf('root child'))
branch = Composite('branch')
branch.add(Leaf('first leaf'))
branch.add(Leaf('second leaf'))
root.add(branch)
root.operation()
