n = int(input())
triangle = []
for i in range(n + 1):
    if i == 0:
        triangle.append([1])
    elif i == 1:
        triangle.append([1, 1])
    else:
        tmp = []
        for j in range(len(triangle[i - 1]) - 1):
            tmp.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        triangle.append([1] + tmp + [1])
print(triangle[n])


##1
##1 1
##1 2 1
##1 3 3 1
##1 4 6 4 1
##1 5 10 10 5 1


