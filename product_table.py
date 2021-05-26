n, m = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == m:
            cnt += 1
print(cnt)
