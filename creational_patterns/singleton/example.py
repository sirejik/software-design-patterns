class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Moneybox(metaclass=MetaSingleton):
    coins = 0

    def put_coin(self):
        self.coins += 1

    def take_coin(self):
        self.coins -= 1


alice = Moneybox()
print(alice.coins)
alice.put_coin()
print(alice.coins)
bob = Moneybox()
print(bob.coins)
bob.take_coin()
print(bob.coins)
