matrix = []
result = None
for i in range(5):
    matrix.append(list(input().split()))
for i, val in enumerate(matrix):
    if '1' in val:
        delta_1 = abs(2 - i)
        delta_2 = abs(2 - matrix[i].index('1'))
        result = delta_1 + delta_2
print(result)
