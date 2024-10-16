import turtle


t = turtle.Turtle()


def draw_filled_circle(size):
    t.begin_fill()
    for _ in range(1):
        t.circle(100)
    t.end_fill()

t.penup()
t.goto(0, 0)  
t.pendown()


t.color("red")


draw_filled_circle(50)
t.end_fill()

turtle.done()