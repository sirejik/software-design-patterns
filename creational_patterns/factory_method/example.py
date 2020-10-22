from abc import ABCMeta, abstractmethod


class Document(metaclass=ABCMeta):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def print(self):
        pass


class ImageDocument(Document):
    def __init__(self, content, size_x, size_y):
        super(ImageDocument, self).__init__(content=content)
        self.size_x = size_x
        self.size_y = size_y

    def print(self):
        print('Printing picture with the following size: {}x{}'.format(self.size_x, self.size_y))


class TextDocument(Document):
    def print(self):
        print('Printing the following text: {}'.format(self.content))


class Application(metaclass=ABCMeta):
    @abstractmethod
    def get_document_manager(self) -> Document:
        pass

    def print_document(self):
        document = self.get_document_manager()
        document.print()


class Paint(Application):
    def get_document_manager(self) -> Document:
        return ImageDocument('picture', 1920, 1080)


class Notepad(Application):
    def get_document_manager(self) -> Document:
        return TextDocument('Hello world')


notepad = Notepad()
notepad.print_document()

paint = Paint()
paint.print_document()
