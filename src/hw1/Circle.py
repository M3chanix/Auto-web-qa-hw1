from hw1.Figure import Figure
from math import pi, sqrt

class Circle(Figure):
    """ Circle figure class"""
    name = 'Circle'

    def __init__(self, *sides):
        if len(sides) == 1:
            super().__init__(*sides)
        else: raise ValueError('Circle should be defined only by radius')

    def area(self) -> float:
        return pi*sqrt(self.sides[0])

    def perimeter(self) -> float:
        return 2*pi*self.sides[0]

