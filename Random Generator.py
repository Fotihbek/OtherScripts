# promo kod generator. Bunda listga kiritilgan raqamlar berilmaydi
from random import randint

max = int(input('Yuqori chegarani kiriting - '))
min = int(input('Pastki chegarani kiriting - '))
soni = input('Nechta son olmoqchisiz? - ')




for i in range(int(soni)):
    yangi_kod = randint(min,max)
    print(i+1,yangi_kod)
