from abc import ABCMeta, abstractmethod


class RasterLib:
    @staticmethod
    def draw_ellipse(x1, y1, x2, y2):
        print('Drawing ellipse in the rectangle with diagonal from ({}, {}) to ({}, {}).'.format(x1, y1, x2, y2))


class VectorLib:
    @staticmethod
    def draw_circle(x, y, r):
        print('Drawing circle at point ({}, {}) with radius {}.'.format(x, y, r))


class AbstractAdapter(metaclass=ABCMeta):
    @abstractmethod
    def circle(self, x, y, r):
        pass


class RasterAdapter(AbstractAdapter, RasterLib):
    def circle(self, x, y, r):
        return self.draw_ellipse(x - r, y - r, x + r, y + r)


class VectorAdapter(AbstractAdapter, VectorLib):
    def circle(self, x, y, r):
        return self.draw_circle(x, y, r)


class DrawingEditor:
    def __init__(self, adapter: AbstractAdapter):
        self.adapter = adapter

    def draw_circle(self, x, y, r):
        self.adapter.circle(x, y, r)


draw_editor = DrawingEditor(RasterAdapter())
draw_editor.draw_circle(5, 5, 1)

draw_editor = DrawingEditor(VectorAdapter())
draw_editor.draw_circle(5, 5, 1)
