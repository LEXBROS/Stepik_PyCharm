chess_desk = []
for col in range(1, 9):
    tmp = [(10 * i + col) for i in range(1, 9)]
    chess_desk.append(tmp)
dct = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'}
pos = input()
pos = int(pos.replace(pos[0], dct[pos[0]]))
for ind, val in enumerate(chess_desk):
    for index, el in enumerate(val):
        if el == pos:
            chess_desk[ind][index] = 'N'
        elif abs(pos - el) in (8, 12, 19, 21):
            chess_desk[ind][index] = '*'
        else:
            chess_desk[ind][index] = '.'
for st in reversed(chess_desk):
    print(*st)
    
