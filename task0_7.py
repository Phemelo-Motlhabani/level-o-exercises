def celsius_to_fahrenheit(degrees_celsius):
    fahrenheit = degrees_celsius * (9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(degrees_fahrenheit):
    celsius = (degrees_fahrenheit - 32) * 5/9
    return celsius


degrees_c = celsius_to_fahrenheit(36)
print(degrees_c)
degrees_f = fahrenheit_to_celsius(96.8)
print(degrees_f)
