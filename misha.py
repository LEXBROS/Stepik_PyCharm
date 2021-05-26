cnt = 0
n, m = map(int, input().split())
str_1 = input()
for _ in range(n - 1):
    str_1 += input()
empty = input()
str_2 = input()
for _ in range(n - 1):
    str_2 += input()
for i, v in enumerate(str_1):
    if v == str_2[i]:
        cnt += 1
print(cnt)
