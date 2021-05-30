def multiply(arg):
    a = arg

    def inner_func(num):
        return a * num

    return inner_func


f_2 = multiply(2)
# здесь мы сохранили первый аргумент(2), f_2 - это теперь функция,
# перемножающая переданный ей элемент на сохраненную 2-ку.
# Для f_2 создалась своя область видимости переменных
print("Умножение 2 на 5 =", f_2(5))
print("Умножение 2 на 15 =", f_2(15))
f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5))
print("Умножение 3 на 15 =", f_3(15))

# Умножение 2 на 5 = 10
# Умножение 2 на 15 = 30
# Умножение 3 на 5 = 15
# Умножение 3 на 15 = 45