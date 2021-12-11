
n = int(input('Necha betli kitobni chiqarmoqchisiz? '))

if n % 4 > 0:
    n = n + (4-n%4)
    
print(int(n/4), 'ta list soling!')
a = int(n/2)
son = int(a/2+1)
list1 = []
list2 = []

def one(son):
    son -= 2
    betlar1 = [a+2]
    for n in range(son):
        bet = betlar1[n] + 2 
        betlar1.append(bet)
    betlar1.reverse()
    return betlar1

def two(son):
    son -= 2
    betlar2 = [1]
    for n in range(son):
        bet = betlar2[n] + 2 
        betlar2.append(bet)
    return betlar2

def three(son):
    son -= 2
    betlar1 = [2]
    for n in range(son):
        bet = betlar1[n] + 2 
        betlar1.append(bet)
    betlar1.reverse()
    return betlar1

def four(son):
    son -= 2
    betlar2 = [a+1]
    for n in range(son):
        bet = betlar2[n] + 2 
        betlar2.append(bet)
    return betlar2

def yakun():
    
    bir = one(son)
    ikki = two(son)
    uch = three(son)
    tort = four(son)

    for n in range(son-1):
        list1.append(bir[n])
        list1.append(ikki[n])
        list2.append(uch[n])
        list2.append(tort[n])
    print('Birinchi tomon -', list1)
    print('Ikkinchi tomon -', list2)

yakun()

