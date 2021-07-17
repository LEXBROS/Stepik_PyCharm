n = int(input())
res = [[] for _ in range(int(n / 2 + 0.5))]
for line in range(int(n / 2 + 0.5)):
    tmp = ['1'.ljust(3) for _ in range(n)]
    for index, val in enumerate(tmp):
        if (line != 0 or line != n - 1) and (index < line or index >= n - line):
            tmp[index] = '0'.ljust(3)
    res[line] = tmp
if n % 2 == 0:
    res = res + res[-1::-1]
else:
    res = res + res[-2::-1]
for lines in res:
    print(*lines, sep='')
