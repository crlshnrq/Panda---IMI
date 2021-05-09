import math


class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def reflect_x(self):
        return self.x, self.y*-1

    def slope_from_origin(self):
        return self.y/self.x

# Esse solução falha quando x1 = x2
    def get_line_to(self, sec):
        a = (sec.y-self.y)/(sec.x-self.x)
        b = self.y - self.x*a
        return int(a), int(b)


def distancia(point1, point2):
    return math.sqrt((point1.getX() - point2.getX())**2 + (point1.getY() - point2.getY())**2)


print(Point(1, 15).get_line_to(Point(1, 5)))




