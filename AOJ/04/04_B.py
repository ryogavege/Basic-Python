import math


def area(x):
    a = round(math.pi * x**2, 6)
    return a


def circ(y):
    c = round(2 * y * math.pi, 6)
    return c


r = round(float(input()), 6)
Area = area(r)
Circ = circ(r)
print(Area, Circ)
