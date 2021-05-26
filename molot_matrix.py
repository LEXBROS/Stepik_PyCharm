n, m = map(int, input().split())
max_sum = sum(int(x) for x in input().split())
max_index = 0
for i in range(1, n):
    tmp = sum(int(x) for x in input().split())
    if max_sum < tmp:
        max_sum = tmp
        max_index = i
print(max_sum, max_index, sep='\n')
