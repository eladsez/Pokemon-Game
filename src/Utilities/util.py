import math

def dist(x1, y1, x2, y2):
    a = math.fabs(x1 - x2)
    b = math.fabs(y1 - y2)
    a = math.pow(a, 2)
    b = math.pow(b, 2)
    return math.sqrt(a + b)

class Line:

    def __init__(self, m):
        self.m = m
        self.d = None

    def findD(self, x, y):
        self.d = y - self.m * x

    def f(self, x):
        return self.m * x + self.d
