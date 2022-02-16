import math

class PointClass():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # x : the value on the x-axis
        # y : the value on the Y-axis
    def show(self):
        return(self.x, self.y)
        # we return the coordinate of this point
        # to write a tuple of 2 elements (float, float)
    def move(self, x, y):
        self.x += x
        self.y += y
        # a method move to change these coordinates
    def distance(self, d):
        x1 = d.x - self.x
        y1 = d.y - self.y 
        return(math.sqrt(x1 ** 2 + y1 ** 2))
        # a method dist that computes the distance between 2 points

point1 = PointClass(2, 3) 
point2 = PointClass(4, 5)    
point1.move(21, -7) 
point2.move(7, -5)
print(point1.show())
print(point2.show())
print(point1.distance(point2))
