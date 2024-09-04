import turtle as t
# Квадрат
t.hideturtle()
t.color('green')
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# t.done()
t.exitonclick()
