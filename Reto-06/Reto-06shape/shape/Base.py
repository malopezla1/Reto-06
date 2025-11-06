from .Point import Point
from .Line import Line

class InvalidShapeError(ValueError):
    """Se lanza cuando los parámetros de una forma son inválidos (ej. lados <= 0)."""

class DegenerateTriangleError(ValueError):
    """Se lanza cuando el triángulo es degenerado (área 0) o no se puede calcular correctamente."""

class Shape:
    def __init__(self, vertices: list[Point], edges: list[Line]):
        self.vertices = vertices
        self.edges = edges

    def is_regular(self, regular: bool) -> bool:
        self.regular = regular
        return self.regular

    def set_vertices(self, vertices: list[Point]) -> list[Point]:
        self.vertices = vertices
        return self.vertices

    def set_edges(self, edges: list[Line]) -> list[Line]:
        self.edges = edges
        return self.edges

    def set_inner_angles(self, angles: list[float]) -> list[float]:
        self.angles = angles
        return self.angles

    def compute_area(self, area: float) -> float:
        self.area = area
        return self.area

    def compute_perimeter(self, perimeter: float) -> float:
        self.perimeter = perimeter
        return self.perimeter

    def compute_inner_angles(self) -> list[float]:
        return self.angles