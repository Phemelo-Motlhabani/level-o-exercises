def area_of_triangle(side_1, side_2, side_3):
    if side_1 + side_2 <= side_3:
        print("Error: Triangle Inequality Theorem")
    if side_1 + side_3 <= side_2:
        print("Error: Triangle Inequality Theorem")
    if side_2 + side_3 <= side_1:
        print("Error: Triangle Inequality Theorem")
    semi_p = 0.5 * (side_1 + side_2 + side_3)
    area_squared = semi_p * (semi_p - side_1) * (semi_p - side_2) * (semi_p - side_3)
    area = area_squared ** (1 / 2)
    return area
