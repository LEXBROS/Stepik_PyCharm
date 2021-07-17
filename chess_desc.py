n, m = map(int, input().split())
chess_desk = []
for col in range(1, n + 1):
    tmp = [(10 * i + col) for i in range(1, m + 1)]
    chess_desk.append(list(map(str, tmp)))
for ind, val in enumerate(chess_desk):
    for index, el in enumerate(val):
        if (int(el[0]) + int(el[1])) % 2 == 0:
            chess_desk[ind][index] = '.'
        else:
            chess_desk[ind][index] = '*'
for st in chess_desk:
    print(*st)
    
