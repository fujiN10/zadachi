import csv
import sqlite3

# dbname = input()
# maxspeed = int(input())
# word = input()
dbname = 'changing.db'
maxspeed = 20
word = 'snow'

con = sqlite3.connect(dbname)
cur = con.cursor()
result = cur.execute('''SELECT change, world, type_id from Changes WHERE speed < ? AND world not like ?''',
                     (maxspeed, '%' + word + '%'))

a = []
for elem in result:
    a.append(elem)
print(a)

b = []
for i in range(len(a)):
    result2 = cur.execute('''SELECT type, relevance from Types WHERE id = ?''', (a[i][2],))
    for el in result2:
        b.append(el)
print(b)

answer = []
answer.append(['no', 'change', 'type', 'world', 'relevance'])
for i in range(len(a)):
    answer.append([i + 1, a[i][0], b[i][0], a[i][1], b[i][1]])
print(answer)

with open('unreal.csv', 'w') as f:
    writer = csv.writer(f, delimiter='#', quotechar='"')
    for el in answer:
        writer.writerow(el)
