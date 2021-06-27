n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range((n + 1) // 2):
    for j in range(n):
        matrix[i][j], matrix[-1 - i][j] = matrix[-1 - i][j], matrix[i][j]
for val in matrix:
    print(*val, sep=' ')
