from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.color import FigureColor


class Rectangle(GeometricFigure):

    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, width_param, height_param):

        self.width = width_param
        self.height = height_param
        self.fc = FigureColor()  # В конструкторе создается объект класса «Цвет фигуры» для хранения цвета.
        self.fc.colorproperty = color_param

    def square(self):
  
        return self.width*self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.square()
        )