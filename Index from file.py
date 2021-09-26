import turtle as t
t.color ('blue')
t.width (2)

f1 = open('numbers.txt', 'r')
read = f1.readlines()
numbers = []
for str in read:
    str = str.rstrip()
    str = str.split(' ')
    lst = []
    for i in range (0, len(str), 3):
        k = int (str[i]), int (str[i + 1]), int (str[i + 2])
        lst.append(k)
    numbers.append(lst)

for i in range (len (numbers)):
    t.penup()
    t.goto(i*50, 0)
    t.pendown()
    t.seth (0)
    for l in numbers[i]:
        if (l[2] == 0):
            t.penup()
        t.left (l[0])
        t.forward (l[1])
        if (l[2] == 0):
            t.pendown()
f1.close()
