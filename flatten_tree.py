def flatten(some_list: list, result_list=None):
    for i in some_list:
        if result_list is None:
            result_list = []
        if isinstance(i, int):
            result_list.append(i)
        else:
            result_list += flatten(i)
    return result_list


print(flatten([[[[9]]], [1, 2], [[8]]]))
