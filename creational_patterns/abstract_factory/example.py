from abc import ABCMeta, abstractmethod


class Steering(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class Tank(Steering):
    def run(self):
        print('Rolls up to the object on tracks.')


class Wheels(Steering):
    def run(self):
        print('Makes several turns of the wheels towards the object.')


class Weapon(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass


class Cannon(Weapon):
    def attack(self):
        print('Shoots at a target with a cannon.')


class Pincers(Weapon):
    def attack(self):
        print('Squeezes target with pincers.')


class RobotFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_steering(self) -> Steering:
        pass

    @abstractmethod
    def get_weapon(self) -> Weapon:
        pass


class Exterminator(RobotFactory):
    def get_steering(self) -> Steering:
        return Tank()

    def get_weapon(self) -> Weapon:
        return Cannon()


class Destroyer(RobotFactory):
    def get_steering(self) -> Steering:
        return Wheels()

    def get_weapon(self) -> Weapon:
        return Pincers()


exterminator = Exterminator()
exterminator.get_steering().run()
exterminator.get_weapon().attack()

destroyer = Destroyer()
destroyer.get_steering().run()
destroyer.get_weapon().attack()
