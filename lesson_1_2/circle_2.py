import turtle as t
# Много кругов
circle = int(input('Введите кол-во кругов '))
diameter = int(input('Введите диаметр начального круга '))
t.hideturtle()

for i in range(circle):
    t.begin_fill()
    t.color('red', 'grey')
    t.circle(diameter + (i * 10))
    t.end_fill()
    t.penup()
    t.forward(75)
    t.pendown()

t.exitonclick()
