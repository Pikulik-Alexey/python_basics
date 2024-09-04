import turtle as t
# Многоугольник
corner = int(input('Введите кол-во углов '))
col = input('Введите цвет на англ. языке ')
t.hideturtle()
t.color(col)
t.begin_fill()
for i in range(corner):
    t.forward(100)
    t.left(360 / corner)
t.end_fill()

t.exitonclick()
