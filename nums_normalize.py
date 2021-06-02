s = input()
res = ''
begin = len(s) % 3
if begin != 0:
    res += s[:begin] + ','

for i in range(begin, len(s), 3):
    res = res + s[i:i + 3] + ','
print(res[:-1])


# print("{:,}".format(int(input())))
