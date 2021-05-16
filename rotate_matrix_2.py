matrix = []
for _ in range(int(input())):
    matrix.append(list(map(int, input().split())))
for i in range(len(matrix) - 1, -1, -1):
    for j in range(len(matrix) - 1, -1, -1):
        print(matrix[j][i], end=' ')
    print()
