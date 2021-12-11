# misol beradigan dastur

from random import randint

a=randint(1,500)
b=randint(1,500)

amal = input('Qaysi amalga oid misol ishlamoqchisiz? + yoki - ')
if amal == '+':
    c=int(input('{} + {} = '.format(a,b)))

    if c == (a + b):
        print('To`g`ri')
    else:
        print('xato aslida javob', a+b)
elif amal == '-':
    c=int(input('{} - {} = '.format(a,b)))

    if c == (a - b):
        print('To`g`ri')
    else:
        print('Xato, aslida javob', a-b)

