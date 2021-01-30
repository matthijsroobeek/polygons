from polygons import RegularPolygon


def main():
    """Main functionality for the Polygon Project."""
    polygon = RegularPolygon(3, 1)
    print(polygon.interior_angle)
    print(polygon.area)


if __name__ == "__main__":
    main()
