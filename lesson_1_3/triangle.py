import turtle as t
# Змейка, узор
t.hideturtle()
t.pensize(3)
t.color('red')
t.rt(50)

for i in range(4, 70, 4):
    t.forward(i)
    t.rt(65)

t.rt(270)
for i in range(68, 0, -4):
    t.forward(i)
    t.rt(65)

t.exitonclick()
