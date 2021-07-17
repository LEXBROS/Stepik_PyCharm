n, m = map(int, input().split())
matr = [[(str(lines + col * n)).ljust(3) for col in range(m)] for lines in range(1, n + 1)]
for el in matr:
    print(*el, sep='')
        
        
