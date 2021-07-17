n, m = map(int, input().split())
res = [[] for _ in range(n)]
el = 1 
while el <= n * m:
    if len(res) == 1 or ((len(res[0]) == 0 or len(res[0]) == len(res[1]) + 1) and len(res[0]) < m):
        res[0].append(str(el).ljust(2))
        el += 1
    else:
        for i in range(1, n):
            if len(res[i]) == m:
                continue
            elif len(res[i - 1]) == len(res[i]) + 2 or len(res[i - 1]) == m:
                res[i].append(str(el).ljust(2))
                el += 1
for val in res:
    print(*val)







## Sample Input 1:
## 3 5
## Sample Output 1:
## 1  2  4  7  10
## 3  5  8  11 13
## 6  9  12 14 15
