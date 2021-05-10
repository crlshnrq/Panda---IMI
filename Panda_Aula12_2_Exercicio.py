
def test(numero, teste):
    return numero is teste


class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY


class Rectangle:

    def __init__(self, ponto, initX, initY):
        self.width = initX
        self.height = initY

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def flip(self):
        alt = self.height
        lar = self.width

        self.width = alt
        self.height = lar

    def contains(self, point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height


r = Rectangle(Point(0, 0), 10, 5)
print(test(r.contains(Point(0, 0)), True))
print(test(r.contains(Point(3, 3)), True))
print(test(r.contains(Point(3, 7)), False))
print(test(r.contains(Point(3, 5)), False))
print(test(r.contains(Point(3, 4.99999)), True))
print(test(r.contains(Point(-3, -3)), False))
