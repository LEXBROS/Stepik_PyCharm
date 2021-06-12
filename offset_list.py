num_list = input().split()
num_list.insert(0, num_list.pop())
print(*num_list)
