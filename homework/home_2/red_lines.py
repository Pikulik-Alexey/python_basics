import turtle as t

t.hideturtle()
t.pensize(5)
t.speed(0)
radius = 100
radius_2 = 90

for j in range(3):
    t.fd(350)
    t.circle(radius, 270)
    t.fd(150)
    t.color((200 + j * 10) / 255, (75 - j * 25) / 255, (45 - j * 15) / 255)
    t.pu()
    t.left(90)
    t.forward(10)
    t.pd()
    t.left(90)
    t.forward(150)
    t.circle(-radius_2, 270)
    t.fd(350)

    for i in range(1):
        t.pu()
        t.right(90)
        t.forward(10)
        t.pd()
        t.right(90)

    radius -= 20
    radius_2 -= 20


t.forward(100)
t.left(135)
t.forward(10)
t.circle(-20, 90)
t.left(135)
t.forward(10)
t.circle(-20, 130)
t.circle(-25, 160)
t.circle(10, 180)
t.circle(-25, 160)
t.fd(28)
t.left(90)

t.fd(173)
t.circle(40, 270)
t.fd(150)

t.exitonclick()
