from math import cos, pi, sin


class RegularPolygon:
    """Class for regular polygons.

    A regular polygon is not any polygon; it's an equiangular (all angles are equal
    in measure) and equilateral (all sides have the same length)."""

    def __init__(self, vertices: int, radius: int = 1):
        """Initialize an object of class Polygon."""
        self.vertices = vertices
        self.outer_radius = radius

    @property
    def interior_angle(self):
        """Return the angle between two adjacent edges of the polygon."""
        return (self.vertices - 2) * pi / self.vertices

    @property
    def inner_radius(self):
        """Return the radius of the biggest possible circle inside the polygon."""
        return cos((pi - self.interior_angle) / 2) * self.outer_radius

    @property
    def edge_length(self):
        """Return the distance between two adjacent vertices of the polygon."""
        return 2 * sin((pi - self.interior_angle) / 2)

    @property
    def area(self):
        """Return the area of the polygon."""
        return self.vertices * 0.5 * self.edge_length * self.inner_radius

