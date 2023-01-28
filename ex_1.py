class Shape:
    def __init__(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError("Cannot add Circle with a non-Circle shape")

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(max(self.radius - other.radius, 0))
        raise TypeError("Cannot subtract Circle with a non-Circle shape")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        raise TypeError("Cannot multiply Circle with a non-Circle shape")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.length + other.length)
        raise TypeError("Cannot add Rectangle with a non-Rectangle shape")

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(max(self.width - other.width, 0), max(self.length - other.length, 0))
        raise TypeError("Cannot subtract Rectangle with a non-Rectangle shape")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Rectangle(self.width * other, self.length * other)
        elif isinstance(other, Rectangle):
            return Rectangle(self.width * other.width, self.length * other.length)
        raise TypeError("Cannot multiply Rectangle with a non-Rectangle shape")


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.width == other.width
        return False

    def __add__(self, other):
        if isinstance(other, Square):
            return Square(self.width + other.width)
        raise TypeError("Cannot add Square with a non-Square shape")

    def __sub__(self, other):
        if isinstance(other, Square):
            return Square(max(self.width - other.width, 0))
        raise TypeError("Cannot subtract Square with a non-Square shape")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Square(self.length * other)
        elif isinstance(other, Rectangle):
            return Square(self.length * other.width)
        raise TypeError("Cannot multiply Square with a non-Square shape")

