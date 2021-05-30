def list_sum_recursive(int_list):
    summa = 0
    if len(int_list) == 0:
        return 0
    else:
        summa += (int_list.pop()) + list_sum_recursive(int_list)
        return summa


print(list_sum_recursive(input()))
