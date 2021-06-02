num = input()
s = lambda x=num: int(x[-1::-1]) if len(x) == 5 else x[0] + x[-1:-6:-1]
print(s())
