import turtle as t

side = int(input('Введите длину стороны '))
side_1 = int(input('Введите длину стороны ромба '))

t.hideturtle()
t.speed(3)

t.begin_fill()
for i in range(2):

    t.width(10)
    t.color('#348888', '#F24405')
    t.forward(side)
    t.left(90)
    t.forward(side / 2)
    t.left(90)
t.end_fill()

t.penup()
t.goto(0, -300)
t.pendown()

t.begin_fill()
for i in range(4):

    t.width(5)
    t.color('red', '#5EC0E6')
    t.left(45)
    t.forward(side_1)
    t.left(45)
t.end_fill()

t.penup()
t.goto(-300, 0)
t.pendown()


t.color('#564040', '#469CAB')
t.begin_fill()
t.forward(150)
t.left(110)
t.forward(100)
t.left(70)
t.forward(75)
t.left(66)
t.forward(100)
t.end_fill()

t.exitonclick()
