# def count_letters(text: str):
#     count_upper = 0
#     count_lower = 0
#     for i in text:
#         if i.isalpha() and i.upper() == i:
#             count_upper += 1
#         elif i.isalpha() and i.lower() == i:
#             count_lower += 1
#     print(f'Количество заглавных символов: {count_upper}')
#     print(f'Количество строчных символов: {count_lower}')

def count_letters(string):
    upper = [i for i in string if i.isupper()]
    lower = [i for i in string if i.islower()]
    print("Количество заглавных символов:", len(upper))
    print("Количество строчных символов:", len(lower))


count_letters('Привет, Старина!!!$|////')
