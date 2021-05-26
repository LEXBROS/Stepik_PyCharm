struct = [[], [], [], []]
beauty = True
for i in range(4):
    struct[i].extend(input())
for j in range(3):
    for k in range(3):
        my_list = [struct[j][k], struct[j + 1][k], struct[j][k + 1], struct[j + 1][k + 1]]
        beauty = beauty and (len(set(my_list)) > 1)
print('Yes' if beauty is True else 'No')
