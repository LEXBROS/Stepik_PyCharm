import os

path = r'/home/lexbros/Рабочий стол/Test_folder_lev1'


def obhod_directory(path, level=1):
    for i in os.listdir(path=path):
        if os.path.isdir(path + '/' + i):
            print('Пошли глубже', os.listdir(path + '/' + i), 'уровень', level)
            obhod_directory(path + '/' + i, level + 1)
            print('Возвращаемся')


obhod_directory(path)
