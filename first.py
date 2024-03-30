with open('fake.txt') as f:
    line = f.readline()
a = []
for i in range(len(list(line))):
    if list(line)[i] == 'R':
        a.append(list(line)[i - 1])
        a.append(list(line)[i + 1])
answer = []
for i in range(len(a)):
    if (a.count(a[i]), a[i]) not in answer:
        answer.append((a.count(a[i]), a[i]))
answer.sort(reverse=True)
finalanswer = []
for i in range(len(answer)):
    if answer[i][0] == answer[0][0]:
        finalanswer.append(answer[i][1])
for el in sorted(finalanswer):
    print(el, end='')


