import re
result = list(map(int, (re.findall(r"\d", input()))))
print(len(result), sum(result))
