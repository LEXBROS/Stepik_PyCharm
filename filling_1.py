n, m = map(int, input().split())
matr = [[str(lines * m + i).ljust(3) for i in range(1, m + 1)] for lines in range(n)]
for el in matr:
    print(*el, sep='')
        
        
