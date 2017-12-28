from math import sin, cos


class Line:

    @staticmethod
    def explicit_equation(a=1, b=1):
        return lambda x: a * x + b

    @staticmethod
    def gradient(x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)

    @staticmethod
    def from_point_and_gradient(y0, k, x1, x2):
        return lambda x: y0 + k * (x2 - x1)

    @staticmethod
    def normal_form(x, y, p, beta):
        return (x * cos(beta)) + (y * sin(beta)) - p

    @staticmethod
    def are_parallel(a1, b1, a2, b2):
        return (a1 / a2) == (b1 / b2)

    @staticmethod
    def are_perpendicular(a1, b1, a2, b2):
        return (a1 * a2) + (b1 * b2) == 0

    @staticmethod
    def distance_from_point(a, b, c):
        return lambda x, y: abs(a * x + b * y + c) / ((a**2 + b**2) ** 0.5)


class Parabola:

    @staticmethod
    def explicit_equation(a, b, c):
        return lambda x: a * x**2 + b * x + c
