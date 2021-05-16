n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n - 1, -1, -1):
    print(*matrix[i], end='\n')
