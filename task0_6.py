def maximum(*numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


max_num = maximum(-2, -33, -1, -9)
print(max_num)
