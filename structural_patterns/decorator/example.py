from abc import ABCMeta, abstractmethod


class DrawingAPI(metaclass=ABCMeta):
    @abstractmethod
    def circle(self, x, y, r):
        pass


class DrawingEditor(DrawingAPI):
    def circle(self, x, y, r):
        print('Drawing circle at point ({}, {}) with radius {}.'.format(x, y, r))


class ResizeEditor(DrawingAPI):
    def __init__(self, drawing_editor: DrawingAPI):
        self.drawing_editor = drawing_editor

    def circle(self, x, y, r):
        print('Change the size of the circle.')
        self.drawing_editor.circle(x, y, r * 2)


paint = DrawingEditor()
paint.circle(5, 5, 2)

paint = ResizeEditor(DrawingEditor())
paint.circle(5, 5, 2)
