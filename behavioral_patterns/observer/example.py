from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, message, log_level):
        pass


class Subscriber1(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message, log_level):
        if log_level != 'DEBUG':
            print('{} received the message: {}'.format(self.name, message))


class Subscriber2(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message, log_level):
        print('{} received the message: {}'.format(self.name, message))


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, message, log_level):
        pass


class Publisher(Subject):
    def __init__(self) -> None:
        self.subscribers = []

    def attach(self, subscriber: Observer):
        self.subscribers.append(subscriber)

    def detach(self, subscriber: Observer) -> None:
        self.subscribers.remove(subscriber)

    def notify(self, message, log_level):
        for subscriber in self.subscribers:
            subscriber.update(message, log_level)

    def check_debug_logging(self):
        self.notify('This is debug message.', 'DEBUG')

    def check_info_logging(self):
        self.notify('This is info message.', 'INFO')


publisher = Publisher()
alice = Subscriber1('Alice')
bob = Subscriber2('Bob')
publisher.attach(alice)
publisher.attach(bob)
publisher.check_debug_logging()
publisher.check_info_logging()
publisher.detach(bob)
publisher.check_debug_logging()
publisher.check_info_logging()
