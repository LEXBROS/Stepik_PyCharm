numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func = lambda x: lambda y: y ** x
print(list(map(func(2), numbers)))
print(list(map(func(3), numbers)))