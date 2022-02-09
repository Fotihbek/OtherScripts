import math

a = int(input('a qiymatni kiriting- '))
b = int(input('b qiymatni kiriting- '))
c = int(input("c qiymatni kiriting- "))
d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print("Tenglama 2 ta ildizga ega!")
    print('x1 = {}'.format(x1))
    print('x2 = {}'.format(x2))

elif d == 0:
    x = (-b + math.sqrt(d))/(2*a)
    print("Tenglama 1 ta ildizga ega!")
    print('x = {}'.format(x))

else:
    print("Tenglama haqiqiy ildizga ega emas!")
