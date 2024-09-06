import turtle as t
# Цветки
t.hideturtle()
t.pensize(3)
t.color('red')
# r = 40
t.fillcolor('green')
t.speed(0)

for i in range(3):
    t.penup()
    t.fd(150)
    t.pendown()
    r = 40
    for k in range(4):
        for i in range(6):
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.rt(60)
        r -= 10


t.exitonclick()
