from hw1.Figure import Figure
from math import sqrt

class Triangle(Figure):
    """Triangle figure class"""
    name = 'Triangle'

    def __init__(self, *sides):
        if len(sides) == 3:
            a, b, c = sides
            if a+b>c and a+c>b and b+c>a:
                super().__init__(*sides)
            else: raise ValueError('Defined triangle could not exist')
        else: raise ValueError('Triangle should be deifned by 3 sides')

    def area(self):
        a, b, c = self.sides
        p = (a+b+c)/2
        return sqrt(p*(p-a)*(p-b)*(p-c))

