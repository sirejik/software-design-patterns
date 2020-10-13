from abc import ABCMeta, abstractmethod


class Car:
    def __init__(self):
        self.engine = None
        self.car_body = None
        self.color = None

    def set_engine(self, engine):
        self.engine = engine

    def set_car_body(self, car_body):
        self.car_body = car_body

    def set_color(self, color):
        self.color = color

    def __repr__(self):
        return 'The car was created with the following parameters:\n\tEngine: {}\n\tCar body: {}\n\tColor: {}'.format(
            self.engine, self.car_body, self.color
        )


class CarBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.product = Car()

    @abstractmethod
    def add_engine(self):
        pass

    @abstractmethod
    def assemble_car_body(self):
        pass

    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def get_car(self):
        pass


class FerrariBuilder(CarBuilder):
    def add_engine(self):
        self.product.set_engine('Ferrari 3.9')

    def assemble_car_body(self):
        self.product.set_car_body('coupe')

    def paint(self):
        self.product.set_color('red')

    def get_car(self):
        return self.product


class Director(metaclass=ABCMeta):
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def build(self):
        self.builder.add_engine()
        self.builder.assemble_car_body()
        self.builder.paint()

    def get_product(self):
        return self.builder.get_car()


car_builder = FerrariBuilder()
director = Director(car_builder)
director.build()
product = director.get_product()
print(product)
