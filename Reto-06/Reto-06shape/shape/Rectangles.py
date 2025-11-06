from .Base import Shape, InvalidShapeError

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        try:
            w = float(width)
            h = float(height)
        except (TypeError, ValueError) as e:
            raise TypeError("Width and height must be numbers") from e

        if w <= 0 or h <= 0:
            raise InvalidShapeError("Width and height must be positive")
        super().__init__(vertices = [], edges = [])
        self.width = width
        self.height = height
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        self.area = self.width * self.height
        return self.area

    def compute_perimeter(self) -> float:
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter

    def compute_inner_angles(self) -> list[float]:
        self.angles = [90.0, 90.0, 90.0, 90.0]
        return self.angles

    def __str__(self) -> str:
        return (
            f"Rectangle\n"
            f"Width: {self.width}, Height: {self.height}\n"
            f"Area: {self.area:.2f}\n"
            f"Perimeter: {self.perimeter:.2f}\n"
            f"Inner Angles: {self.angles}"
        )

class Square(Rectangle):
    def __init__(self, side_length: float):
        self.side_length = float(side_length)
        super().__init__(side_length, side_length)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        self.area = self.side_length ** 2
        return self.area

    def compute_perimeter(self) -> float:
        self.perimeter = 4 * self.side_length
        return self.perimeter

    def __str__(self) -> str:
        return (
            f"Square\n"
            f"Side Length: {self.side_length}\n"
            f"Area: {self.area:.2f}\n"
            f"Perimeter: {self.perimeter:.2f}\n"
            f"Inner Angles: {self.angles}"
        )