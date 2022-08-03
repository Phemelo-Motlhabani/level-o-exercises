def area_of_triangle(side_1, side_2, side_3):
    semi_perimeter = 0.5 * (side_1 + side_2 + side_3)
    area_squared = semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3)
    return area_squared ** (1 / 2)

triangle_area = area_of_triangle(3, 4, 5)
print(triangle_area)
