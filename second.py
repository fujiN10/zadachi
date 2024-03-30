import csv, json

with open('worlds.csv') as f:
    reader = csv.reader(f, delimiter='&')
    rows = [(r[1], r[2], r[3]) for r in reader]
    rows = rows[1:]
answer = {}
for el in rows:
    key = el[0]
    value = [[el[1], el[2]]]
    if key not in answer.keys():
        answer.update({key: value})
    else:
        answer[key].extend(value)
print(answer)

with open('thin_spot.json', 'w') as f:
    json.dump(answer, f)


