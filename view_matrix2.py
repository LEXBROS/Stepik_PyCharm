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
print()
for col in range(m):
    for rows in range(col, n * m, m):
        print(matrix[rows], end=' ')
    print()
