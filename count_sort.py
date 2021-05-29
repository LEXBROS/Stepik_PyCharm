records = [0 for _ in range(-100, 101)]
n = int(input())
s = list(map(int, input().split()))
for i in range(n):
    records[s[i] + 100] += 1
for index, value in enumerate(records):
    if value != 0:
        for j in range(value):
            print(index - 100, end=' ')
