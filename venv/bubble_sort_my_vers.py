q = int(input())
s = list(map(int, input().split()))
changes = 1
all_count = 0
while changes != 0:
    for i in range(0, q - 1):
        if s[i] > s[i + 1]:
            s[i], s[i + 1] = s[i + 1], s[i]
            changes += 1
            all_count += 1
    if changes == 1:
        changes = 0
    else:
        changes = 1
print(*s)
print(all_count)
