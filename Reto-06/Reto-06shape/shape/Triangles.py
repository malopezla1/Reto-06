from math import sqrt, acos, degrees, atan
from .Base import Shape, InvalidShapeError

class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise InvalidShapeError("Triangle sides must be positive")
        if not (side_a + side_b > side_c and side_a + side_c > side_b 
                and side_b + side_c > side_a):
            raise InvalidShapeError("Triangle sides do not satisfy triangle inequality")
        
        super().__init__(vertices = [], edges = [])
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def compute_area(self) -> float:
        self.area = (self.side_a * self.side_b) / 2
        return self.area
    
    def compute_perimeter(self) -> float:
        self.perimeter = self.side_a + self.side_b + self.side_c
        return self.perimeter
    
    def compute_inner_angles(self) -> list[float]:
        angle_a = 60
        angle_b = 60
        angle_c = 60
        self.angles = [angle_a, angle_b, angle_c]
        return self.angles
    
    def __str__(self) -> str:
        return (
            f"Triangle\n"
            f"Side A: {self.side_a}, Side B: {self.side_b}, Side C: {self.side_c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.angles}"
        )


class Isosceles(Triangle):
    def __init__(self, side_equal: float, base: float):
        super().__init__(side_equal, side_equal, base)
        self.side_equal = side_equal
        self.base = base
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        height = sqrt(self.side_equal**2 - (self.base / 2)**2)
        self.area = height * self.base / 2
        return self.area
    
    def compute_perimeter(self) -> float:
        self.perimeter = self.side_equal * 2 + self.base
        return self.perimeter

    def compute_inner_angles(self) -> list[float]:
        height = sqrt(self.side_equal**2 - (self.base / 2)**2)
        # Angle of the opposite vertex
        angle_vertex = degrees(2 * (acos(height / (self.side_equal))))
        # Angles of the base
        angles_base = (180 - angle_vertex) / 2 
        self.angles = [angles_base, angles_base, angle_vertex]
        return self.angles
    
    def __str__(self) -> str:
        return (
            f"IsoscelesTriangle\n"
            f"Same Length: {self.side_equal}\n"
            f"Base: {self.base}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.angles}"
        )


class Equilateral(Triangle): 
    def __init__(self, side_length: float):
        super().__init__(side_length, side_length, side_length)
        self.side_length = side_length
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        self.area = (sqrt(3) / 4) * self.side_length ** 2
        return self.area

    def compute_perimeter(self) -> float:
        self.perimeter = 3 * self.side_length
        return self.perimeter

    def compute_inner_angles(self) -> list[float]:
        self.angles = [60, 60, 60]
        return self.angles

    def __str__(self) -> str:
        return (
            f"Equilateral Triangle\n"
            f"Side Length: {self.side_length}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.angles}"
        )


class Scalene(Triangle):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        s = (self.side_a + self.side_b + self.side_c) / 2
        self.area = sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return self.area
    
    def compute_perimeter(self) -> float:
        self.perimeter = self.side_a + self.side_b + self.side_c
        return self.perimeter

    def compute_inner_angles(self) -> list[float]:
        angle_a = degrees(acos((self.side_b**2 + self.side_c**2 - self.side_a**2) 
                                         / (2 * self.side_b * self.side_c)))
        angle_b = degrees(acos((self.side_a**2 + self.side_c**2 - self.side_b**2) 
                                         / (2 * self.side_a * self.side_c)))
        angle_c = 180 - angle_a - angle_b
        self.angles = [angle_a, angle_b, angle_c]
        return self.angles
    
    def __str__(self) -> str:
        return (
            f"Scalene Triangle\n"
            f"Side A: {self.side_a}, Side B: {self.side_b}, Side C: {self.side_c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.angles}"
        )

class Trirectangle(Triangle):
    def __init__(self, side_a: float, side_b: float):
        side_c = sqrt(side_a**2 + side_b**2)
        super().__init__(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        self.area = (self.side_a * self.side_b) / 2
        return self.area
    
    def compute_perimeter(self) -> float:
        self.perimeter = self.side_a + self.side_b + self.side_c
        return self.perimeter
    
    def compute_inner_angles(self) -> list[float]:
        self.angles = [90, degrees(atan(self.side_b / self.side_a)), 
                       degrees(atan(self.side_a / self.side_b))]
        return self.angles

    def __str__(self) -> str:
        return (
            f"Trirectangle\n"
            f"Side A: {self.side_a}, Side B: {self.side_b}, Side C: {self.side_c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.angles}"
        )