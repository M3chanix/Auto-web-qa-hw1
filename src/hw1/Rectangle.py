from hw1.Figure import Figure

class Rectangle(Figure):
    """Rectangle figure class"""
    name = 'Rectangle'

    def __init__(self, *sides):
        if len(sides) != 2:
            raise ValueError('Rectangle should be defined by 2 sides')
        else: 
            super().__init__(*sides)

    def area(self) -> float:
        return self.sides[0] * self.sides[1]

    def perimeter(self) -> float:
        return 2 * self.sides[0] + 2* self.sides[1]

