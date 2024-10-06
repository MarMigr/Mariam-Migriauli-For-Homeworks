import turtle


t = turtle.Turtle()

t.penup()             
t.goto(-50,-50)       
t.pendown()   


for _ in range(8):
    t.forward(100)    # Move forward by 100 units (side length)
    t.left(45)        # Turn left by 45 degrees


turtle.done()
