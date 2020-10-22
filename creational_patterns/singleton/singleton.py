"""
Ensures that a class has only one instance and provides a global access point to it.
"""


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class MyClass(metaclass=MetaSingleton):
    counter = 0

    def increase_counter(self):
        self.counter += 1


concrete_object = MyClass()
print(concrete_object.counter)
concrete_object.increase_counter()
print(concrete_object.counter)
concrete_object2 = MyClass()
print(concrete_object2.counter)
