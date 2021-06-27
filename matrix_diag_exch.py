n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    matrix[i][i], matrix[-1 - i][i] = matrix[-1 - i][i], matrix[i][i]
for val in matrix:
    print(*val, sep=' ')
