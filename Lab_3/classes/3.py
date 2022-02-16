class Shape:
    area = 0
    def area(self):
        print(f'{self.length * self.width}')


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f'{self.length * self.width}')


s = Rectangle(5, 4)
s.area()
