class Point:
    def __init__(self, x: float, y: float):
        try:
            self._x = float(x)
            self._y = float(y)
        except (TypeError, ValueError) as e:
            raise TypeError("Point coordinates must be numbers") from e
    
    def compute_distance(self) -> float:
        return (self._x**2 + self._y**2) ** 0.5

    def get_x(self) -> float:
        return self._x

    def set_x(self, x: float) -> None:
        try:
            self._x = float(x)
        except (TypeError, ValueError) as e:
            raise TypeError("x coordinate must be a number") from e

    def get_y(self) -> float:
        return self._y

    def set_y(self, y: float) -> None:
        try: 
            self._y = float(y)
        except (TypeError, ValueError) as e:
            raise TypeError("y coordinate must be a number") from e