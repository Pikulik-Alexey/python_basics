import turtle as t

t.hideturtle()


for j in range(3):
    t.begin_fill()
    for i in range(4):
        t.color('green')
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.pu()
    t.fd(150)
    t.pd()


t.exitonclick()
