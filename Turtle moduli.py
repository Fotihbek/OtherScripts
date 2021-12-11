from turtle import Turtle, Screen
import random

oyna = Screen()
oyna.title('My first game')
#oyna.mainloop() oynani qoldirish cmd da...

ramka = Turtle()
ramka.color('red')
ramka.pensize(4)
ramka.speed(0)
ramka.hideturtle()
ramka.up()
ramka.goto(200, 200)
ramka.down()
ramka.goto(200, -200)
ramka.goto(-200, -200)
ramka.goto(-200, 200)
ramka.goto(200, 200)

katak = Turtle()
katak.color('green')
katak.pensize(4)
katak.speed(0)
katak.hideturtle()
katak.up()
katak.goto(-50, -200)
katak.down()
katak.goto(-50, -170)
katak.goto(-180, -170)
katak.goto(-180, -200)
katak.goto(-50, -200)

a = random.randrange(-180,200)
b = random.randrange(-180,200)
soqqa = Turtle()
soqqa.shape('circle')
soqqa.color('blue')
soqqa.speed(0)
soqqa.up()
soqqa.goto(1,78)

qadam_x = 3
qadam_y = 2
while True:
    x, y = soqqa.position()
    if x + qadam_x >= 200 or x + qadam_x <= -200:
        qadam_x=-qadam_x
    if y + qadam_y >= 200 or y + qadam_y <= -200:
        qadam_y=-qadam_y
    if x + qadam_x <= -50 and y + qadam_y <= -180:
        break
    soqqa.goto(x+qadam_x, y+qadam_y)



