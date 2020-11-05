from __future__ import annotations

import json

import xml.etree.ElementTree as ElementTree

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, exporter: Exporter):
        pass


class Dot(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def accept(self, exporter: Exporter):
        return exporter.export_dot_information(self)


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def accept(self, exporter: Exporter):
        return exporter.export_circle_information(self)


class Square(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def accept(self, exporter: Exporter):
        return exporter.export_square_information(self)


class Exporter(metaclass=ABCMeta):
    @abstractmethod
    def export_dot_information(self, element: Dot):
        pass

    @abstractmethod
    def export_circle_information(self, element: Circle):
        pass

    @abstractmethod
    def export_square_information(self, element: Square):
        pass


class XMLExporter(Exporter):
    def export_dot_information(self, dot: Dot):
        dot_node = ElementTree.Element('dot')
        x_node = ElementTree.SubElement(dot_node, 'x')
        x_node.text = str(dot.x)
        y_node = ElementTree.SubElement(dot_node, 'y')
        y_node.text = str(dot.y)

        return dot_node

    def export_circle_information(self, circle: Circle):
        circle_node = ElementTree.Element('circle')
        x_node = ElementTree.SubElement(circle_node, 'x')
        x_node.text = str(circle.x)
        y_node = ElementTree.SubElement(circle_node, 'y')
        y_node.text = str(circle.y)
        y_node = ElementTree.SubElement(circle_node, 'radius')
        y_node.text = str(circle.radius)

        return circle_node

    def export_square_information(self, square: Square):
        square_node = ElementTree.Element('square')
        x1_node = ElementTree.SubElement(square_node, 'x1')
        x1_node.text = str(square.x1)
        y1_node = ElementTree.SubElement(square_node, 'y1')
        y1_node.text = str(square.y1)
        x2_node = ElementTree.SubElement(square_node, 'x2')
        x2_node.text = str(square.x2)
        y2_node = ElementTree.SubElement(square_node, 'y2')
        y2_node.text = str(square.y2)

        return square_node


class JSONExporter(Exporter):
    def export_dot_information(self, dot: Dot):
        return {
            'shape': 'dot',
            'x': dot.x,
            'y': dot.y
        }

    def export_circle_information(self, circle: Circle):
        return {
            'shape': 'circle',
            'x': circle.x,
            'y': circle.y,
            'radius': circle.radius
        }

    def export_square_information(self, square: Square):
        return {
            'shape': 'square',
            'x1': square.x1,
            'y1': square.y1,
            'x2': square.x2,
            'y2': square.y2
        }


shapes = [
    Dot(1, 1),
    Circle(1, 1, 0.5),
    Square(0, 0, 2, 2),
    Dot(1.5, 1),
    Dot(0.5, 1),
    Circle(3, 1, 1)
]
xml_exporter = XMLExporter()
xml_shapes = ElementTree.Element('shapes')
for shape in shapes:
    xml_shapes.append(shape.accept(xml_exporter))

ElementTree.dump(xml_shapes)

json_exporter = JSONExporter()
json_shapes = []
for shape in shapes:
    json_shapes.append(shape.accept(json_exporter))

print(json.dumps(json_shapes))
