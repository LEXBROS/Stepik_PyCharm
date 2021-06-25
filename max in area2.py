from math import ceil

n = int(input())
begin = 1
end = n - 1
quarter_left = []
quarter_right = []
for i in range(ceil(n / 2)):
    tmp = list(map(int, input().split()))
    quarter_left += tmp[:begin]
    quarter_right += tmp[end:]
    begin += 1
    end -= 1
begin = ceil(n / 2) - 1
end = ceil(n / 2)
for i in range(n - ceil(n / 2)):
    tmp = list(map(int, input().split()))
    quarter_left += tmp[:begin]
    quarter_right += tmp[end:]
    begin -= 1
    end += 1

print(quarter_left)
print(quarter_right)
