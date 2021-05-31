import json

with open('group_people.json', 'r') as file:
    data = json.load(file)

result = {}

for i in data:
    result[i['id_group']] = 0
    for j in i['people']:
        if j['gender'] == 'Female' and j['year'] > 1977:
            result[i['id_group']] += 1

for key, value in sorted(result.items(), key=lambda pare: -pare[1]):
    print(key, value)
