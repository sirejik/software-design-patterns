import time


class Memento:
    def __init__(self, state):
        self._state = state
        self._timestamp = time.time()

    def get_state(self):
        return self._state

    def get_timestamp(self):
        return self._timestamp


class Editor:
    def __init__(self):
        self._text = ''

    def add_text(self, text):
        self._text += text

    def print_state(self):
        print(self._text)

    def save(self) -> Memento:
        return Memento(self._text)

    def restore(self, memento):
        self._text = memento.get_state()


class Caretaker:
    def __init__(self, editor: Editor):
        self.snapshots = []
        self.editor = editor

    def save(self):
        snapshot = self.editor.save()
        self.snapshots.append(snapshot)
        print('State for \'{}\' was saved with timestamp {}.'.format(self.editor, snapshot.get_timestamp()))
        return len(self.snapshots) - 1

    def restore(self, snapshot_index):
        snapshot = self.snapshots[snapshot_index]
        self.editor.restore(snapshot)
        print('State for \'{}\' was restored with timestamp {}.'.format(self.editor, snapshot.get_timestamp()))


text_editor = Editor()
text_editor.add_text('Hello world!')
text_editor.print_state()
caretaker = Caretaker(text_editor)
index = caretaker.save()
text_editor.add_text(' Bye!')
text_editor.print_state()
caretaker.restore(index)
text_editor.print_state()
