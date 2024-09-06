import turtle as t

t.speed(2)
t.ht()
t.pensize(5)
t.right(60)
for r in range(90, 10, -20):

    for i in range(6):
        t.color(255 / 255, 165 / 255, (255 - r) / 255)
        t.fillcolor(162 / 255, (255 - r) / 255, 255 / 255)
        t.begin_fill()
        for k in range(3):
            t.forward(r)
            t.left(120)
        t.end_fill()
        t.rt(60)


t.exitonclick()
