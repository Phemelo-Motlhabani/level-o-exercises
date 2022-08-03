def maximum(*numbers):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


max_num = maximum(9, 2, 12, 36, 36, 17, 13, 55, 45, 8, 42, 31, 28, 2, 8)
print(max_num)