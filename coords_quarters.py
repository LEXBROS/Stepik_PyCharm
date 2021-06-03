n = int(input())
dct = {'Первая четверть': 0, 'Вторая четверть': 0, 'Третья четверть': 0, 'Четвертая четверть': 0}
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        continue
    else:
        if x > 0 and y > 0:
            dct['Первая четверть'] += 1
        elif x < 0 < y:
            dct['Вторая четверть'] += 1
        elif x < 0 and y < 0:
            dct['Третья четверть'] += 1
        else:
            dct['Четвертая четверть'] += 1
for key, value in dct.items():
    print(key, value, sep=': ')
