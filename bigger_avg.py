n = int(input())
res = []
tmp_list = []
tmp = 0
for i in range(n):
    tmp_list = list(map(int, input().split()))
    for j in tmp_list:
        tmp += (j > sum(tmp_list) / len(tmp_list))
    res.append(tmp)
    tmp = 0
print(*res, sep='\n')
