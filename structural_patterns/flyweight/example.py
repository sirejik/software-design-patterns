import random


class Lamp:
    def __init__(self, color):
        self.color = color


class LampFactory:
    lamps = {}

    @staticmethod
    def get_lamp(color) -> Lamp:
        return LampFactory.lamps.setdefault(color, Lamp(color))


class TreeBranch:
    def __init__(self, branch_number):
        self.branch_number = branch_number

    def hang(self, lamp):
        print('Hang {} lamp on branch {}.'.format(lamp.color, self.branch_number))


class Tree:
    branches = {}

    def get_branch(self, number):
        return self.branches.setdefault(number, TreeBranch(number))

    def hang_lamps_on_tree(self):
        for _ in range(0, 100):
            color = random.choice(['red', 'green', 'blue', 'yellow'])
            branch_number = random.randint(1, 10)
            self.get_branch(branch_number).hang(LampFactory.get_lamp(color))


tree = Tree()
tree.hang_lamps_on_tree()
print('Number of lamps: {}.'.format(len(LampFactory.lamps)))
print('Number of branches: {}.'.format(len(Tree.branches)))
