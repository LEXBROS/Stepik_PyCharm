n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_t = list(zip(*matrix))
all_digits = []
summa = sum(matrix[0])
first_diag = []
second_diag = []
for i in range(n):
    first_diag.append(matrix[i][i])
    second_diag.append(matrix[i][-1 - i])
for val in matrix:
    all_digits += val
flag = True
for i in range(1, (n ** 2) + 1):
    flag = flag and (i in all_digits)
if flag is True:
    for j in range(n):
        flag = flag and sum(matrix[j]) == summa
        flag = flag and sum(matrix_t[j]) == summa
    if flag is True:
        flag = flag and sum(first_diag) == summa
        flag = flag and sum(second_diag) == summa
        print('YES' if flag is True else 'NO')
    else:
        print('NO')
else:
    print('NO')
