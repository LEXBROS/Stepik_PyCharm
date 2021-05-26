names = {}
collect = []
for i in range(1, int(input()) + 1):
    uniq = input()
    postfix = str(collect.count(uniq)) if collect.count(uniq) > 0 else ''
    names[i] = [uniq, postfix]
    collect.append(uniq)
for value in names.values():
    print('OK' if value[1] == '' else value[0] + value[1])
