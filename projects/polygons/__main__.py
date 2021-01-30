from polygons import RegularPolygon
import matplotlib.pyplot as plt


def main():
    """Main functionality for the Polygon Project."""
    vertices = []
    areas = []
    for number_of_vertices in range(3, 18):
        vertices.append(number_of_vertices)
        areas.append(RegularPolygon(number_of_vertices).area)

    plt.plot(vertices, areas)
    plt.show()


if __name__ == "__main__":
    main()
