from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self, n):
        pass


class Swordsman(Unit):
    def attack(self, n):
        print('\t' * n + 'Swordsman \'{}\' strikes with a sword.'.format(self.name))


class Archer(Unit):
    def attack(self, n):
        print('\t' * n + 'Archer \'{}\' shoots.'.format(self.name))


class Knight(Unit):
    def attack(self, n):
        print('\t' * n + 'Knight \'{}\' attacks on horseback.'.format(self.name))


class Squad(Unit):
    def __init__(self, name):
        super(Squad, self).__init__(name)
        self.children = []

    def add(self, leaf: Unit):
        self.children.append(leaf)

    def attack(self, n=0):
        print('\t' * n + 'The squad \'{}\' attack with the following composition:'.format(self.name))
        for child in self.children:
            child.attack(n + 1)


division = Squad('Division')
division.add(Knight('Richard the Lionheart'))
platoon = Squad('Platoon')
platoon.add(Archer('Robin Hood'))
platoon.add(Swordsman('Duncan Macleod'))
division.add(platoon)
division.attack()
