matrix = []
for _ in range(int(input())):
    matrix.append(list(map(int, input().split())))
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[j][i], end=' ')
    print()
