def maximum(int_1, int_2, int_3):
    if int_1 >= int_2 and int_1 >= int_3:
        return int_1
    elif int_2 >= int_1 and int_2 >= int_3:
        return int_2
    elif int_3 >= int_1 and int_3 >= int_2:
        return int_3


max_num = maximum(1, 2, 3)
print(max_num)
