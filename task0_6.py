def maximum(int_1, int_2, int_3):
    if int_1 > int_2 and int_1 > int_3:
        return int_1
    if int_2 > int_1 and int_2 > int_3:
        return int_2
    if int_3 > int_1 and int_3 > int_2:
        return int_3
