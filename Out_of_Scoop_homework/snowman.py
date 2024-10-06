import turtle


t = turtle.Turtle()
t.speed(20)

def draw_filled_man(size):
    t.begin_fill()
    for _ in range(1):
        t.circle(size)
    t.end_fill()

def draw_filled_triangle(size):
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()



t.penup()
t.goto(-100,100)  
t.pendown()


t.color("lightblue")

draw_filled_man(50) #1 


t.penup()
t.goto(-100,-100) 
t.pendown()


draw_filled_man(100)  #2


t.penup()
t.goto(-100,-400)  
t.pendown()


draw_filled_man(150)   

t.penup()
t.goto(-130,150)  
t.pendown()

t.color("black")

draw_filled_man(1)

t.penup()
t.goto(-65,150)  
t.pendown()

t.color("black")

draw_filled_man(1)

#for nose 
t.penup()
t.goto(-99,140) 
t.pendown()

t.color("orange")

draw_filled_triangle(10)

t.hideturtle() 


turtle.done()

