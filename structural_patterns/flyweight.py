class Flyweight:
    def __init__(self, name):
        self.name = name


class FlyweightFactory:
    flyweights = {}

    @staticmethod
    def get_flyweight(number) -> Flyweight:
        return FlyweightFactory.flyweights.setdefault(number, Flyweight(number))


class ConcreteFlyweight:
    def __init__(self, number):
        self.number = number

    def print(self, flyweight: Flyweight):
        print("Flyweight {} for {}".format(flyweight.name, self.number))


class UnsharedConcreteFlyweight:
    def __init__(self):
        self.concrete_flyweights = {}

    def get_flyweight(self, number) -> ConcreteFlyweight:
        return self.concrete_flyweights.setdefault(number, ConcreteFlyweight(number))

    def add_flyweight(self, number, name):
        return self.get_flyweight(number).print(FlyweightFactory.get_flyweight(name))


object_list = UnsharedConcreteFlyweight()
for i in range(1000):
    object_list.add_flyweight(i, 'object_{}'.format(i % 5))

print(len(FlyweightFactory.flyweights))
print(len(object_list.concrete_flyweights))
