# СОРТИРОВКА ВСТАВКАМИ
n = int(input())
unsorted = list(map(int, input().split()))
point_search = 1
while point_search <= len(unsorted) - 1:
    for i in range(1, len(unsorted)):
        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
    point_search += 1
print(*unsorted)
