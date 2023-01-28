class Shape:
    DEFAULT_INNER_COLOR = "white"
    DEFAULT_OUTER_COLOR = "black"

    @staticmethod
    def create_default_circle(radius):
        return Circle(radius, Shape.DEFAULT_INNER_COLOR, Shape.DEFAULT_OUTER_COLOR)

    @staticmethod
    def create_default_rectangle(width, length):
        return Rectangle(width, length, Shape.DEFAULT_INNER_COLOR, Shape.DEFAULT_OUTER_COLOR)

    @staticmethod
    def create_default_square(side_length):
        return Square(side_length, Shape.DEFAULT_INNER_COLOR, Shape.DEFAULT_OUTER_COLOR)

    @staticmethod
    def color_shapes(list_of_shapes, inner_color, border_color):
        for shape in list_of_shapes:
            shape.inner_color = inner_color
            shape.outer_color = border_color
