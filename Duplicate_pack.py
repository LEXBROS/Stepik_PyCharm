s = input().replace(' ', '')
result=[]
for ch in s:
    if len(result) == 0 or (len(result) != 0 and ch not in result[-1]):
        result.append(list(ch))
    elif ch in result[-1]:
        result[-1].append(ch)
print(result)
        

        
