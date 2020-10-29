"""
Encapsulates a request as an object, thereby allowing clients to set parameters for processing the corresponding
requests, enqueue or log requests, and support cancellation.
"""
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self):
        self.receiver = Receiver()

    def execute(self):
        self.receiver.foo()


class Receiver:
    @staticmethod
    def foo():
        print('Command foo was executed.')


class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command: Command):
        self.history.append(command)
        command.execute()

    def print_history(self):
        for command in self.history:
            print(command)


class Client:
    def __init__(self):
        self.invoker = Invoker()

    def execute_foo_command(self):
        command = ConcreteCommand()
        self.invoker.execute_command(command)

    def print_executed_commands(self):
        self.invoker.print_history()


client = Client()
client.execute_foo_command()
client.execute_foo_command()
client.print_executed_commands()
