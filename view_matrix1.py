n, m = int(input()), int(input())
matrix = []
for i in range(n * m):
    matrix.append(input())
begin = 0
while begin < n * m:
    for i in range(begin, begin + m):
        print(matrix[i], end=' ')
    print()
    begin += m
