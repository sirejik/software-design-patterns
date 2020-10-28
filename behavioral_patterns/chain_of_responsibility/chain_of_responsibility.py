"""
Avoids binding the sender of the request to its recipient, giving multiple objects a chance to process the request.
Chains recipient objects and passes the request along that chain until it is processed.
"""
from abc import ABC, ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_request(self):
        pass


class AbstractHandler(Handler, ABC):
    next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self.next_handler = handler
        return handler

    def handle_request(self):
        if self.next_handler:
            return self.next_handler.handle_request()

        return None


class ConcreteHandler1(AbstractHandler):
    def handle_request(self):
        print('Handle by ConcreteHandler1')
        return super().handle_request()


class ConcreteHandler2(AbstractHandler):
    def handle_request(self):
        print('Handle by ConcreteHandler2')
        return super().handle_request()


concrete_handler1 = ConcreteHandler1()
concrete_handler2 = ConcreteHandler2()

concrete_handler1.set_next(concrete_handler2)
concrete_handler1.handle_request()
