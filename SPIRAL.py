from math import ceil

n = int(input())  # считал размер массива
result = [['' for _ in range(n)] for _ in range(n)]
# print(result)
begin = 0
end = n

value = 1

for cycle in range(ceil(n / 2)):
    if end != begin:
        for i in range(begin, end):
            result[begin][i] = str(value)
            value += 1
        for j in range(begin + 1, end):
            result[j][end - 1] = str(value)
            value += 1
        for i in range((end - 2), (begin - 1), -1):
            result[end - 1][i] = str(value)
            value += 1
        for j in range((end - 2), begin, -1):
            result[j][begin] = str(value)
            value += 1
        begin += 1
        end -= 1
    else:
        result[begin][end] = str(value)
for k in range(n):
    print(*result[k])
