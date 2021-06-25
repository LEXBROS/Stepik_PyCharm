matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_t = list(zip(*matrix))
print(*matrix)  # [1, 2, 3] [4, 5, 6] [7, 8, 9]
print(matrix_t)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
