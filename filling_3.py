n = int(input())
matr = []
for lines in range(n):
    matr.append([0 for _ in range(n)])
for f_index, f_val in enumerate(matr):
    for s_index, s_val in enumerate(f_val):
        if s_index == n - f_index - 1 or s_index == f_index:
            matr[f_index][s_index] = 1
for el in matr:
    print(*el)
        
