def area_of_triangle(s_1, s_2, s_3):
    if s_1 + s_2 <= s_3:
        print("Error: Triangle Inequality Theorem")
    if s_1 + s_3 <= s_2:
        print("Error: Triangle Inequality Theorem")
    if s_2 + s_3 <= s_1:
        print("Error: Triangle Inequality Theorem")
    s = 0.5 * (s_1 + s_2 + s_3)
    area_squared = s * (s - s_1) * (s - s_2) * (s - s_3)
    # Heron's Formula states area = sqrt(s * (s - s_1) * (s - s_2) * (s - s_3))
    # where s_1, s_2 and s_3 are sides of a traingle
    area = area_squared ** (1 / 2)
    return area
