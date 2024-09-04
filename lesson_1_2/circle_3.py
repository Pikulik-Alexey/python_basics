import turtle as t
# Много кругов
t.speed(10)
t.hideturtle()

for i in range(10, 70, 5):
    t.color('green')
    t.circle(i)
    t.left(35)
t.exitonclick()
