import math
class AreaFinding:
    def triangle_area(self, base, height):
        return 0.5 * base * height
    def rectangle_area(self, length, width):
        return length * width
    def circle_area(self, radius):
        return math.pi * radius ** 2
    def display_all_areas(self, triangle_base, triangle_height, rectangle_length, rectangle_width, circle_radius):
        print("Area of a triangle with base", triangle_base, "and height", triangle_height, ":", self.triangle_area(triangle_base, triangle_height))
        print("Area of a rectangle with length", rectangle_length, "and width", rectangle_width, ":", self.rectangle_area(rectangle_length, rectangle_width))
        print("Area of a circle with radius", circle_radius, ":", round(self.circle_area(circle_radius), 2))

if __name__ == "__main__":
    area_finder = AreaFinding()
    area_finder.display_all_areas(10, 5, 10, 5, 7)
