from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, editor):
        self.editor = editor

    @abstractmethod
    def execute(self):
        pass


class AddCommand(Command):
    def __init__(self, editor, text):
        super(AddCommand, self).__init__(editor)
        self.text = text

    def execute(self):
        self.editor.add_sentence(self.text)


class UndoCommand(Command):
    def execute(self):
        self.editor.remove_last_sentence()


class PrintCommand(Command):
    def execute(self):
        text = self.editor.get_text()
        print(' '.join(text))


class CopyCommand(Command):
    def execute(self):
        return self.editor.get_text().copy()


class PasteCommand(Command):
    def __init__(self, editor, sentences):
        super(PasteCommand, self).__init__(editor)
        self.sentences = sentences

    def execute(self):
        for sentence in self.sentences:
            self.editor.add_sentence(sentence)


class Editor:
    def __init__(self):
        self.text = []

    def add_sentence(self, sentence):
        print('Sentence \'{}\' were added to the text.'.format(sentence))
        self.text.append(sentence)

    def remove_last_sentence(self):
        print('The last sentence was removed from the text.')
        del self.text[-1]

    def get_text(self):
        print('All saved sentences were returned.')
        return self.text


class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command: Command):
        if not isinstance(command, PrintCommand):
            self.history.append(command)

        return command.execute()

    def print_history(self):
        for command in self.history:
            print(command.__class__.__name__)


class Application:
    def __init__(self):
        self.invoker = Invoker()
        self.editor = Editor()
        self.clipboard = None

    def type_text(self, text):
        self.invoker.execute_command(AddCommand(self.editor, text))

    def undo(self):
        self.invoker.execute_command(UndoCommand(self.editor))

    def print_text(self):
        self.invoker.execute_command(PrintCommand(self.editor))

    def copy(self):
        self.clipboard = self.invoker.execute_command(CopyCommand(self.editor))

    def paste(self):
        if self.clipboard is not None:
            self.invoker.execute_command(PasteCommand(self.editor, self.clipboard))

    def print_history(self):
        self.invoker.print_history()


application = Application()
application.type_text('Hello')
application.type_text('Word')
application.undo()
application.type_text('world!')
application.copy()
application.paste()
application.print_text()
application.print_history()
