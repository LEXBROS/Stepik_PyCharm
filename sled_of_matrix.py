n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
sum = 0
for i in range(n):
    sum += matrix[i][i]
print(sum)
