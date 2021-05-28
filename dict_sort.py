driver_dict = {}
while True:
    s = input()
    if s == 'конец':
        break
    else:
        tmp = s.split(', ')
        k, v = tmp[0], tmp[1]
        if k in driver_dict.keys():
            driver_dict[k][0] += int(v)
            driver_dict[k][1] += 1
        else:
            driver_dict[k] = [int(v), 1]
for key, value in sorted(driver_dict.items(), key=lambda pare: (-(pare[1][0] / pare[1][1]), pare[0])):
    print(key, value[0] / value[1])

r = iter(input(), )
# Нужно расположить таксистов в порядке убывания
# их средней оценке и вывести имя каждого таксиста
# и его среднюю оценку в отдельной строке.
# В случае совпадения средних оценок расположить
# таксистов нужно отсортировать имена таксистов по алфавиту
