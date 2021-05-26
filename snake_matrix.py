cnt = 0
n, m = map(int, input().split())
my_list = []
begin, end, step = 0, m, 1
while cnt != n:
    my_list.append([i for i in range(begin, end, step)])
    begin, end = end, end + m
    cnt += 1
rev = False
for i in range(len(my_list)):
    my_list[i].sort(reverse=rev)
    print(*my_list[i])
    if rev is False:
        rev = True
    else:
        rev = False
