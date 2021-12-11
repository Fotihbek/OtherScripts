def fibonachchi_top(son):
    son -=2
    fibonachchilar = [1, 1]
    for n in range(son):
        fibonach = fibonachchilar[n] + fibonachchilar[n+1] 
        fibonachchilar.append(fibonach)
    return fibonachchilar
print(fibonachchi_top(int(input("Dastlabki nechta fibonachchi sonlarni topmoqchisiz? "))))
