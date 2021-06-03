my_list = list(map(int, input().split()))
marks = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i + 1] > my_list[i]]
print(len(marks))
