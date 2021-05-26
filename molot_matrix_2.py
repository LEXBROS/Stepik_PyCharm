n, m = map(int, input().split())
matrix = [list(int(i) for i in input().split()) for _ in range(n)]
maximum = max(matrix[0])
maximum_index = matrix[0].index(maximum)
maximum_row = 0
for j in range(1, n):
    if maximum < max(matrix[j]):
        maximum = max(matrix[j])
        maximum_index = matrix[j].index(maximum)
        maximum_row = j
print(maximum)
print(maximum_row, maximum_index)
