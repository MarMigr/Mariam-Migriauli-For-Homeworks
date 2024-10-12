import turtle


t = turtle.Turtle()


t.speed(3)


def draw_filled_triangle(size):
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Function to draw a star
def draw_star(size):
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144) 
    t.end_fill()



t.penup()
t.goto(-50, 150)  
t.pendown()


t.color("green")

draw_filled_triangle(100)


t.penup()
t.goto(-75, 100)  
t.pendown()


draw_filled_triangle(150)


t.penup()
t.goto(-100, 50)  
t.pendown()


draw_filled_triangle(200)


t.penup()
t.goto(-125, 0)  
t.pendown()


draw_filled_triangle(250)


t.penup()
t.goto(-25, 0)  
t.pendown()


t.color("brown")  
t.begin_fill()
for _ in range(2):
    t.forward(50)  
    t.right(90)
    t.forward(70) 
    t.right(90)
t.end_fill()


t.penup()
t.goto(-25, 252)  
t.pendown()


t.color("yellow")


draw_star(50)
t.end_fill()



t.hideturtle()



turtle.done()
