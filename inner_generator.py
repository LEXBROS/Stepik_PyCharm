vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

# for i in vector:
#     for j in i:


s = [j for i in vector for j in i]

print(s)
