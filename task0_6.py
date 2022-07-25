def maximum(int_1, int_2, int_3):
    if int_1 >= int_2 and int_1 >= int_3:
        return int_1
    elif int_2 >= int_3:
        return int_2
    else:
        return int_3


max_num = maximum(9, 2, 7)
print(max_num)
