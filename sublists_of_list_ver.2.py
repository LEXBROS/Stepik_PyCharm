s = list(input().replace(' ', ''))
result = [[], ]
for diap in range(1, len(s) + 1):
    for begin in range(0, len(s) - diap + 1):
        result.append(list(s[begin:begin + diap]))
print(result)
