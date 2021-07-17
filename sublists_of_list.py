s = list(input().replace(' ', ''))
result = [[], ]
for el in s:
    result.append(list(el))
for diap in range(2, len(s) + 1):
    for begin in range(0, len(s) - diap + 1):
        result.append(list(s[begin:begin + diap]))
print(result)
