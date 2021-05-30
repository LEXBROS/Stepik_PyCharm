# функция quick_sort должна выполнить сортировку
def quick_sort(s):
    left_list = []
    center_list = []
    right_list = []
    if len(s) == 1 or s == []:
        return s
    else:
        for i in s:
            if i < s[0]:
                left_list.append(i)
            if i == s[0]:
                center_list.append(i)
            if i > s[0]:
                right_list.append(i)
        return quick_sort(left_list) + center_list + quick_sort(right_list)


print(quick_sort([16,19,2,12,20,15,20,15]))
