n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_rotate = [[] for _ in range(n)]
for i in range(n):
    for j in range(n - 1, -1, -1):
        matrix_rotate[i].append(matrix[j][i])
for val in matrix_rotate:
    print(*val, sep=' ')
