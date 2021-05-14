stack = []
n = input()
if len(n) == 2 and (n == '()' or n == '{}' or n == '[]'):
    print('YES')
else:
    try:
        for i in n:
            if i in ('(', '[', '{'):
                stack.append(i)
            elif i in (')', ']', '}'):
                ret = stack[-1] + i
                if ret == '()' or ret == '[]' or ret == '{}':
                    del stack[-1]
                    continue
                else:
                    break
        print('YES' if len(stack) == 0 else 'NO')
    except IndexError:
        print('NO')
