def is_simple(num):
    cnt_s = 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            cnt_s += 1
    return cnt_s == 2

cnt = 0
n = int(input())
for i in range(n + 1, n * 2):
    if is_simple(i):
        cnt += 1
print(cnt)
