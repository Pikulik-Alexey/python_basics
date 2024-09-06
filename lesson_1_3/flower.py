import turtle as t
# Цветок
t.hideturtle()
t.pensize(3)
t.color('red')
r = 40
t.fillcolor('green')

for i in range(4):
# for i in range(40, 0, -10):

    for i in range(6):
        t.begin_fill()
        t.color(255 / 255, 165 / 255, (r - 40) / 255)
        t.fillcolor(162 / 255, ((r - 40) * 6) / 255, 255 / 255)
        t.circle(r)
        t.end_fill()
        t.rt(60)
    r -= 10


t.exitonclick()
