n = int(input())
lst, i = [], 0
while i < n:
    lst += list(map(int, input().split()))[:i + 1]
    i += 1
print(max(lst))
