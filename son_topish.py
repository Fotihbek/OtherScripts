import random

def dastur(maks):
    tasodif = random.randrange(1,maks+1)
    myTahmin = int(input(f'1 dan {maks} gacha son o\'yladim topa olasizmi? - '))
   
    for n in range(maks+1):
        if tasodif==myTahmin:
            print(f'Topdingiz! O\'ylagan sonim {myTahmin} edi. {n+1} ta tahmin bilan topdingiz.')
            break
        elif tasodif < myTahmin:
            print(f'O\'ylagan sonim, {myTahmin} dan kichik' )
        elif tasodif > myTahmin:
            print(f'O\'ylagan sonim, {myTahmin} dan katta' )
        myTahmin = int(input('Tahmin qilgan soningizni kiriting - '))
        global x1
        x1 = n + 1
    
def user(maks):
    x2 = 0
    quyi = 1
    yuqori = maks
    input(f'1 dan {maks} gacha son o\'ylang va ixtiyoriy tugmani bosing!')
    while True:
        x2 += 1
        if quyi != yuqori:
            pctahmin = random.randint(quyi, yuqori)
        else:
            pctahmin = quyi

        print('Tahminimcha o\'ylagan soningiz -', pctahmin)
        tekshir = input('Agar to\'g\'ri topgan bo\'lsam - "t", o\'ylagan soningizdan kichik bo\'lsa - "-", katta bo\'lsa - "+" kiriting!')
        
        if tekshir == '+':
            quyi = pctahmin + 1
        elif tekshir == '-':
            yuqori = pctahmin - 1
        else:
            print(':)')
            break
       
    print(f'{x2} ta tahmin bilan topdim!')
    global a
    a = x2
            
def taqqos():
    if x1 > a:
        print(f' {a}:{x1} hisobda yutdim, tabriklang!')
    elif x1 < a:
        print(f' {x1}:{a} hisobda yutdingiz, tabriklayman') 
    else:
        print(f'Durang! {x1}:{a}')

maks = int(input('Keling o\'ylagan sonni topish o\'ynaymiz, yuqori chegarani kiriting - '))
dastur(maks)
user(maks)
taqqos()
#Alhamdulillah