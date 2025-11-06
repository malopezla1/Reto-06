from shape import Rectangle, Square, Isosceles, Equilateral, Scalene, Trirectangle

if __name__ == "__main__":
    figures = [
        Rectangle(4, 5),
        Square(4),
        Isosceles(5, 6),
        Equilateral(4),
        Scalene(4, 5, 6),
        Trirectangle(3, 4)
    ]

    for figure in figures:
        print(figure)
        print("-" * 40)