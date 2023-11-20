import sql
import files
import new
import random

user_name = input("Enter your user name")
li = []

for i in range(0, 6):
    a = random.randint(1, 5)
    for j in range(1, 5):
        c = random.randint(1, 5)
        a = str(a) + str(c)
    b = str(a)  # print(b)
    result = files.exsit(b, open("diceware.txt"))
    li.append(result)

final = new.joi(li)

i = 0
p = new.hexa(final)

date = new.date1()
code = int(random.randrange(10000000))
sql.insert_code(code, user_name, p, date)
