import turtle as t

t.speed(3)
t.ht()
t.pensize(5)
t.right(45)
for r in range(70, 30, -10):

    for i in range(6):
        t.color(255 / 255, 165 / 255, ((r - 40) * 6) / 255)
        t.fillcolor(162 / 255, ((r - 40) * 6) / 255, 255 / 255)
        t.begin_fill()
        for k in range(4):
            t.forward(r)
            t.left(90)
        t.end_fill()
        t.rt(60)


t.exitonclick()
