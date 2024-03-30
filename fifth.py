from flask import Flask
import sqlite3
import json

app = Flask(__name__)

with open('fear.json') as f:
    data = json.load(f)

dbname = data['filename']
fears = data['fears']
level = data['level']

con = sqlite3.connect(dbname)
cur = con.cursor()
a = []

for i in range(len(fears)):
    result = cur.execute('''SELECT advice, fear, level from Advices WHERE level >= ? AND fear = ?''',
                         (level, fears[i]))
    for el in result:
        a.append(el)
a.sort()

for i in range(len(a)):
    a[i] = {'advice': a[i][0],
            'fear': a[i][1],
            'level': a[i][2]}


@app.route('/fear')
def fear():
    print(a)
    return a


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
