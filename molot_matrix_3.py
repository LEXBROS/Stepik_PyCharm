n, m = map(int, input().split())
sp_dict = {}
for i in range(n):
    tmp = list(map(int, input().split()))
    sp_dict[i] = [max(tmp), sum(tmp)]
concur = []
maximum = sp_dict[0][0]
for key, value in sp_dict.items():
    if maximum < value[0]:
        maximum = value[0]
for key, value in sp_dict.items():
    if value[0] == maximum:
        concur.append(key)
winner_key = concur[0]
winner_sum = sp_dict[winner_key][1]
for i in concur:
    if winner_sum < sp_dict[i][1]:
        winner_sum = sp_dict[i][1]
        winner_key = i
print(winner_key)
