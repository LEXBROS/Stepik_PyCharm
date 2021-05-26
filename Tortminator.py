h, w = map(int, input().split())
lines = []
cnt = 0
for _ in range(h):
    line = input()
    if 'S' in line:
        tmp = [i for i in line]
        lines.append(tmp)
    else:
        cnt += w
for columns in range(w):
    Flag = True
    for rows in range(len(lines)):
        Flag = Flag and 'S' not in lines[rows][columns]
    if Flag is not True:
        Flag = True
    else:
        cnt += len(lines)
        continue
print(cnt)
