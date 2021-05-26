n, m = map(int, input().split())
cnt = 0
my_list = ['.' * (m + 2)]
for i in range(n):
    my_list.append('.' + input() + '.')
my_list.append('.' * (m + 2))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if my_list[i][j] == '.':
            pattern = [my_list[i - 1][j], my_list[i][j - 1], my_list[i][j + 1], my_list[i + 1][j]]
            if set(pattern) == {'.'}:
                cnt += 1
print(cnt)
