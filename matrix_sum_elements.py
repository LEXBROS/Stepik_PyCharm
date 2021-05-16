n, m = map(int, input().split())
matrix = []
columns_sum, line_sum = [], []
for _ in range(n):
    ad_ = list(map(int, input().split()))
    matrix.append(ad_)
    line_sum.append(sum(ad_))
for i in range(m):
    tmp_sum = 0
    for j in range(n):
        tmp_sum += matrix[j][i]
    columns_sum.append(tmp_sum)
print(*line_sum)
print(*columns_sum)
