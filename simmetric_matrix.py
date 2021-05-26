symmetric = True
matrix = []
for _ in range(int(input())):
    matrix.append(list(map(int, input().split())))
j = len(matrix)
while j != 0:
    for i in range(j):
        symmetric = symmetric and matrix[j - 1][i] == matrix[i][j - 1]
    j -= 1
print('Yes' if symmetric else 'No')
