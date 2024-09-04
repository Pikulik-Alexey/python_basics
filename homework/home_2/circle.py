import turtle as t

circle = int(input('Введите кол-во кругов '))
diametr = int(input('Введите диаметр '))
t.hideturtle()
t.speed(5)
for i in range(circle):
    t.begin_fill()
    t.color((50 + i * 20) / 255, (193 - i * 15) / 255, (143 - i * 5) / 255)
    t.circle(diametr + (i * 10))
    t.penup()
    t.forward(75)
    t.pendown()
    t.end_fill()


t.exitonclick()
