def game_round(timur, ruslan):
    my_dict = {'камень': ['ящерица', 'ножницы'],
               'ножницы': ['ящерица', 'бумага'],
               'бумага': ['Спок', 'камень'],
               'ящерица': ['Спок', 'бумага'],
               'Спок': ['камень', 'ножницы']
               }
    if timur in my_dict.keys() and ruslan in my_dict[timur]:
        return 'Тимур'
    if timur == ruslan:
        return 'ничья'
    else:
        return 'Руслан'


print(game_round(input(), input()))
