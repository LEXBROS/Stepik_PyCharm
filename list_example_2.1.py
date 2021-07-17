n = int(input())
example = [val for val in range(1, n + 1)]
result = [example[:i] for i in range(1, n + 1)]
print(*result, sep='\n')
