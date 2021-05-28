actors_dict = {}
for _ in range(int(input())):
    nominant = input()
    if nominant not in actors_dict:
        actors_dict[nominant] = 1
    else:
        actors_dict[nominant] += 1
if len(actors_dict) != 1:
    cnt = 0
    for key, value in sorted(actors_dict.items(), key=lambda pare: (-pare[1])):
        if cnt == 0 or cnt == len(actors_dict) - 1:
            print(f'{key}, {value}')
        cnt += 1
else:
    for k, v in actors_dict.items():
        print(f'{k}, {v}')
        print(f'{k}, {v}')
