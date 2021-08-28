import csv

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    index = next(reader).index('Primary Type')
    dict_of_types = {}
    for row in reader:
        if row[index] not in dict_of_types.keys():
            dict_of_types[row[index]] = 1
        else:
            dict_of_types[row[index]] += 1
for key,  value in sorted(dict_of_types.items(), key=lambda pare: -pare[1]):
    print(key, value)
