n, k = int(input()), int(input())
circle = [i for i in range(1, n + 1)]
deleting = k - 1
while len(circle) > 1:
    delta = deleting in range(0, len(circle))
    if delta is True:
        del circle[deleting]
        deleting += k - 1
    else:
        deleting = deleting % len(circle)
print(*circle)
