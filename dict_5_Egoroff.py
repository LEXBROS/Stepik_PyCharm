my_dict = {}
for i in input().lower():
    if i.isalpha() and i not in my_dict.keys():
        my_dict[i] = 1
    elif i.isalpha() and i in my_dict.keys():
        my_dict[i] += 1
print(my_dict)
