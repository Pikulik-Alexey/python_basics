import turtle as t

base = int(input('Введите длину '))

t.hideturtle()

for j in range(3):
    t.begin_fill()
    for i in range(20, 8, -4):
        t.color('#1FF008')
        t.forward(base)
        t.left(120)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(base - base / 3)
    t.right(90)
    t.pendown()

# t.begin_fill()
# for i in range(3):
#     t.color('#87E019')
#     t.forward(base)
#     t.left(120)
# t.end_fill()

# t.penup()
# t.left(90)
# t.forward(base - base / 3)
# t.right(90)
# t.pendown()

# t.begin_fill()
# for i in range(3):
#     t.color('#A8E063')
#     t.forward(base)
#     t.left(120)
# t.end_fill()


t.exitonclick()
