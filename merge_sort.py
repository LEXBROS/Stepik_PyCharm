import time

# функция merge_two_list должна объединить два списка
def merge_two_list(a, b):
    new_list = []
    i, j = 0, 0
    while i != len(a) and j != len(b):
        if i != len(a) and j != len(b) and a[i] <= b[j]:
            new_list.append(a[i])
            i += 1
            # print(i, new_list)
        if i != len(a) and j != len(b) and a[i] >= b[j]:
            new_list.append(b[j])
            j += 1
            # print(j, new_list)
    if i == len(a):
        return new_list + b[j:]
    elif j == len(b):
        return new_list + a[i:]


# функция merge_sort должна выполнить сортировку
def merge_sort(s):
    if len(s) < 2:
        return s
    else:
        return merge_two_list(merge_sort(s[: len(s) // 2]), merge_sort(s[len(s) // 2:]))


start_time = time.time()
print(merge_sort(
    [2, 1, 4, 3, 6, 5, 10, 2, 6, 8, 9, 7, 5, 6, 7, 8, 9, 5, 6, 3, 25, 4, 56, 6, 5, 5, 5, 5, 6, 9, 5, 4, 5, 2, 1, 4, 3,
     6, 5, 10, 2, 6, 8, 9, 7, 5, 6, 7, 8, 9, 5, 6, 3, 25, 2, 1, 4, 3, 6, 5, 10, 2, 6, 8, 9, 7, 5, 6, 7, 8, 9, 5, 6, 3,
     25, 2, 1, 4, 3, 6, 5, 10, 2, 6, 8, 9, 7, 5, 6, 7, 8, 9, 5, 6, 3, 25, 2, 1, 4, 3, 6, 5, 10, 2, 6, 8, 9, 7, 5, 6, 7,
     8, 9, 5, 6, 3, 25, 2, 1, 4, 3, 6, 5, 10, 2, 6, 8, 9, 7, 5, 6, 7, 8, 9, 5, 6, 3, 25]))
print(time.time() - start_time)
