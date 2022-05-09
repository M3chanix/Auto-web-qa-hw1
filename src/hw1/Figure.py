class Figure():
    """ A base geometric figure class"""
    name = 'Figure'

    def __init__(self, *sides):
        self.sides = sides

    def area(self) -> float:
        return 0

    def perimeter(self) -> float:
        return sum(x for x in self.sides)

    def add_area(self, other_figure) -> float:
        if isinstance(other_figure, Figure):
            return self.area() + other_figure.area()
        else:
            raise ValueError('Given value is not a Figure instance')

