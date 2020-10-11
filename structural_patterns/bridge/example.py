from abc import ABCMeta, abstractmethod


class DrawingAPI(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def circle(self, x, y, r):
        pass


class LineDrawingAPI(DrawingAPI):
    def circle(self, x, y, r):
        print('Drawing circle at point ({}, {}) with radius {}.'.format(x, y, r))


class FillDrawingAPI(DrawingAPI):
    def circle(self, x, y, r):
        print('Drawing circle at point ({}, {}) with radius {} and filling it.'.format(x, y, r))


class DrawingEditor(metaclass=ABCMeta):
    def __init__(self, drawing_api: DrawingAPI):
        self.drawing_api = drawing_api

    @abstractmethod
    def draw_circle(self, x, y, r):
        pass


class Paint(DrawingEditor):
    def __init__(self, implementor: DrawingAPI):
        super(Paint, self).__init__(implementor)

    def draw_circle(self, x, y, r):
        return self.drawing_api.circle(x, y, r)


draw_editor = Paint(LineDrawingAPI())
draw_editor.draw_circle(5, 5, 1)

draw_editor = Paint(FillDrawingAPI())
draw_editor.draw_circle(5, 5, 1)
