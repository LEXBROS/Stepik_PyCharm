def chanked(s, piece):
    s = s.replace(' ', '')
    result=[]
    for ch in s:
        if len(result) == 0 or (len(result) != 0 and len(result[-1]) == piece):
            result.append(list(ch))
        else:
            result[-1].append(ch)
    return result

st = input()
piece = int(input())

print(chanked(st, piece))
        

        
