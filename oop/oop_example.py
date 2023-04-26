class Point:

    default_colour = "green"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"The point is from {self.x} to {self.y}"

    def draw(self):
        print(f"Drawing from {self.x} to {self.y} ... ")


p1 = Point(4, 6)
p2 = Point(2, 3)
p1.draw()
p2.draw()
print(isinstance(p1, Point))
print(p1)
print(p2)
print(Point.default_colour)
print(p1.default_colour)
print(p2.default_colour)
