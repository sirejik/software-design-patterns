from abc import abstractmethod


class CarBuilder:
    def build(self):
        self.create_car_body()
        self.insert_engine()

    @abstractmethod
    def create_car_body(self):
        pass

    @abstractmethod
    def insert_engine(self):
        pass


class AutomaticBuilder(CarBuilder):
    def create_car_body(self):
        print('The body is quickly assembled by a robot.')

    def insert_engine(self):
        print('The robot inserts the engine in the car.')


class HandmadeBuilder(CarBuilder):
    def create_car_body(self):
        print('The man forges a car body for a long time.')

    def insert_engine(self):
        print('With great difficulty, the man inserts the engine into the body.')


car_builder = AutomaticBuilder()
car_builder.build()
car_builder = HandmadeBuilder()
car_builder.build()
