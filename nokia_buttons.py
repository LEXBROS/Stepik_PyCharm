buttons = {1: ['.', ',', '?', '!', ':'],
           2: ['A', 'B', 'C'],
           3: ['D', 'E', 'F'],
           4: ['G', 'H', 'I'],
           5: ['J', 'K', 'L'],
           6: ['M', 'N', 'O'],
           7: ['P', 'Q', 'R', 'S'],
           8: ['T', 'U', 'V'],
           9: ['W', 'X', 'Y', 'Z'],
           0: [' ']}
msg = input().upper()
for sym in msg:
    for key, value in buttons.items():
        if sym in value:
            print(str(key)*(value.index(sym) + 1), end='')

# Sample Input 1:
# Hello, World!
# Sample Output 1:
# 4433555555666110966677755531111
