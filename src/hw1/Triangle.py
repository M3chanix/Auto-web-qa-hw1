from hw1.Figure import Figure
from math import sqrt
from functools import cache

class Triangle(Figure):
    """Triangle figure class"""
    _name = 'Triangle'

    def __init__(self, *sides):
        if len(sides) == 3:
            a, b, c = sides
            if a+b>c and a+c>b and b+c>a:
                super().__init__(*sides)
            else: return None # раньше здесь просто поднимал ошибку, но по условию нужно вернуть None - не знаю зачем, класс всё равно создаётся
        else: raise ValueError('Triangle should be deifned by 3 sides')

    @property
    @cache
    def area(self):
        a, b, c = self._sides
        p = (a+b+c)/2
        return sqrt(p*(p-a)*(p-b)*(p-c))

