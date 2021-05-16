matrix = []
for i in range(int(input())):
    matrix.append(list(map(int, input().split()))[i])
print(sum(matrix))
