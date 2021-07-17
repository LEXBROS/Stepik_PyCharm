n, m = map(int, input().split())
template = [str(i).ljust(3) for i in range(1, m + 1)]
print(*template, sep='')
for _ in range(n - 1):
    tmp = template[0]
    del template[0]
    template.append(tmp)
    print(*template, sep='')

