class Circle:
    pi = 3.14

    def __init__(self, radius=None):
        self.radius = radius

    def print_area(self):
        return Circle.pi * (self.radius * self.radius)



