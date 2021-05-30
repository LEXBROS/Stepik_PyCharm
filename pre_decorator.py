def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for key, value in kwargs.items():
        print(key, value, type(value))


print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two=2, one=1, three=3)
