"""
Without violating the encapsulation, it fixes and takes out of the object its internal state so that later the object
can be restored in it.
"""


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def print_state(self):
        print('Current state: {}.'.format(self._state))

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()


class Caretaker:
    def __init__(self, originator: Originator):
        self.snapshots = []
        self.originator = originator

    def save(self):
        self.snapshots.append(self.originator.save())
        print('State for \'{}\' was saved.'.format(self.originator))
        return len(self.snapshots) - 1

    def restore(self, snapshot_index):
        self.originator.restore(self.snapshots[snapshot_index])
        print('State for \'{}\' was restored.'.format(self.originator))


def foo():
    originator = Originator(5)
    originator.print_state()
    caretaker = Caretaker(originator)
    snapshot_index = caretaker.save()
    originator.set_state(1)
    originator.print_state()
    caretaker.restore(snapshot_index)
    originator.print_state()


foo()
