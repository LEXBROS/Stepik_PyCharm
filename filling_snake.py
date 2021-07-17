n, m = map(int, input().split())
string = 0
res = []
while len(res) != n:
    if string % 2 == 0:
        tmp = [str(i).ljust(2) for i in range(string * m + 1, string * m + m + 1)]
        res.append(tmp)
        string += 1
    else:
        tmp = [str(i).ljust(2) for i in range(string * m + m, string * m, -1)]
        res.append(tmp)
        string += 1
for line in res:
    print(*line)    

