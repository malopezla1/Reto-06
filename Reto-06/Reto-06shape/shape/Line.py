from .Point import Point
from math import sqrt

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        return sqrt((self.end.get_x() - self.start.get_x()) ** 2 +
                    (self.end.get_y() - self.start.get_y()) ** 2)
