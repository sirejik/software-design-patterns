from abc import ABC, ABCMeta, abstractmethod
from collections import namedtuple

Account = namedtuple('Account', ('sms', 'phone', 'email'))


class Notifier(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, message, account):
        pass


class AbstractNotifier(Notifier, ABC):
    next_notifier: Notifier = None

    def set_next(self, logger: Notifier) -> Notifier:
        self.next_notifier = logger
        return logger

    def notify(self, message, account):
        if self.next_notifier:
            return self.next_notifier.notify(message, account)

        return None


class SMSNotifier(AbstractNotifier):
    def notify(self, message, account):
        if account.sms is True and account.phone is not None:
            print('Send SMS \'{}\' to phone number \'{}\'.'.format(message, account.phone))

        return super().notify(message, account)


class MailNotifier(AbstractNotifier):
    def notify(self, message, account):
        if account.email is not None:
            print('Send mail with the text \'{}\' to email \'{}\'.'.format(message, account.email))

        return super().notify(message, account)


class CallNotifier(AbstractNotifier):
    def notify(self, message, account):
        if account.phone is not None:
            print('Call by phone \'{}\'.'.format(account.phone))

        return super().notify(message, account)


notifier = SMSNotifier()
mail_notifier = MailNotifier()
call_notifier = CallNotifier()

notifier.set_next(mail_notifier)
mail_notifier.set_next(call_notifier)

alice = Account(sms=True, phone='8-800-400-20-10', email='alice@mail.com')
notifier.notify('Hello', alice)

bob = Account(sms=False, phone='8-100-200-40-80', email=None)
notifier.notify('Hello', bob)
