import turtle


t = turtle.Turtle()

t.penup()             
t.goto(-100,-150)       
t.pendown()   


for _ in range(10):
    t.forward(125)    
    t.left(36)       


turtle.done()
