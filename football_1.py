my_list = []
cnt = 0
for _ in range(int(input())):
    my_list.extend(input().split())
for i in range(0, len(my_list), 2):
    for j in range(1, len(my_list), 2):
        if my_list[i] == my_list[j]:
            cnt += 1
print(cnt)
