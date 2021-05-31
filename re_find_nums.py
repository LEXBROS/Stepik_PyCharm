import re

pattern_2x = r'(\b\d{2}\b)'
pattern_3x = r'(\b\d{3}\b)'

with open('numbers.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    d_2 = list(map(int, re.findall(pattern_2x, text)))
    d_3 = re.findall(pattern_3x, text)
print(len(d_3), sum(d_2), sep=',')
