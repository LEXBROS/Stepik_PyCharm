import json

managers = {}

with open('manager_sales.json', 'r') as file:
    data = json.load(file)

for i in data:
    for key, value in i.items():
        if key == 'manager':
            name = value['first_name'] + ' ' + value['last_name']
            managers[name] = 0
        if key == 'cars':
            for j in value:
                managers[name] += j['price']
for n, total in sorted(managers.items(), key=lambda pare: pare[1]):
    print(n, total)
