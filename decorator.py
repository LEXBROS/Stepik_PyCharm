def decorator(func):

    def inner_func():
        print('декоратор старт')
        func()
        print('декоратор финиш')

    return inner_func


def say_hello():
    print('Hello, world!!!')


say_hello = decorator(say_hello)
say_hello()

# декоратор - это функция, которая принимает функцию и возвращает функцию, но с расширенным функционалом
