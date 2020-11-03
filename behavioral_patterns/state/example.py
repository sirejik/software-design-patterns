from abc import ABCMeta, abstractmethod


class Duck:
    def __init__(self):
        self.state = WaterState()

    def change_state(self, new_state):
        if new_state == 'water':
            self.state = WaterState()
        elif new_state == 'ground':
            self.state = GroundState()
        elif new_state == 'air':
            self.state = AirState()

    def move(self):
        self.state.move()


class State(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass


class GroundState(State):
    def move(self):
        print('The duck walks along the ground.')


class AirState(State):
    def move(self):
        print('The duck flies in the sky.')


class WaterState(State):
    def move(self):
        print('The duck swims in the water.')


context = Duck()
context.move()
context.change_state('air')
context.move()
context.change_state('ground')
context.move()
