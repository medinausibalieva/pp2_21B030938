import math

class Find_area():
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def show(self):
        print(f'{self.length * self.height}')

a = Find_area(5, 6)    
a.show()  

