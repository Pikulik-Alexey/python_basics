import turtle as t
# Звезда
corner = 9
t.hideturtle()
t.begin_fill()
t.color(255/255, 165/255, 6/255)
for i in range(corner):
    t.forward(100)
    t.right(360 * 2 / corner)
t.end_fill()

t.exitonclick()
