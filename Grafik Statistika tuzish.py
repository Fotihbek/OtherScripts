# Grafik tuzish uchun

import pygal

nom1 = input('Ijtimoiy tarmoq nomini kiriting- ')
qiymat1 = input('{}ning 3 ta qiymatini kiriting- '.format(nom1))
nom2 = input('Ijtimoiy tarmoq nomini kiriting- ')
qiymat2 = input('{}ning 3 ta qiymatini kiriting- '.format(nom2))
nom3 = input('Ijtimoiy tarmoq nomini kiriting- ')
qiymat3 = input('{}ning 3 ta qiymatini kiriting- '.format(nom3))

a1,b1,c1 = qiymat1.split(',')
a2,b2,c2 = qiymat2.split(',')
a3,b3,c3 = qiymat3.split(',')

grafik = pygal.Line()
grafik.title = 'Statistika'
grafik.x_labels = ['Avgust', 'Sentabr', 'Oktabr']
grafik.add(nom1, [int(a1), int(b1), int(c1)])
grafik.add(nom2, [int(a2), int(b2), int(c2)])
grafik.add(nom3, [int(a3), int(b3), int(c3)])
grafik.render_in_browser()
