import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(3)

# Function to draw a filled triangle (tree layers)
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
        t.right(144)  # Angle for a 5-pointed star
    t.end_fill()



# Position for the first triangle (top of the tree)
t.penup()
t.goto(-50, 150)  # Adjust the starting position for the top triangle
t.pendown()

# Set the tree color to green
t.color("green")

# Draw the top triangle (smallest)
draw_filled_triangle(100)

# Move to position for the second triangle
t.penup()
t.goto(-75, 100)  # Move down and center for the second triangle
t.pendown()

# Draw the second triangle
draw_filled_triangle(150)

# Move to position for the third triangle
t.penup()
t.goto(-100, 50)  # Move down for the third triangle
t.pendown()

# Draw the third triangle
draw_filled_triangle(200)

# Move to position for the fourth triangle
t.penup()
t.goto(-125, 0)  # Move down for the fourth triangle
t.pendown()

# Draw the fourth triangle (largest)
draw_filled_triangle(250)

# Move to position for the trunk
t.penup()
t.goto(-25, 0)  # Move down to draw the trunk
t.pendown()

# Draw the trunk (a rectangle)
t.color("brown")  # Change color to brown for the trunk
t.begin_fill()
for _ in range(2):
    t.forward(50)  # Width of the trunk
    t.right(90)
    t.forward(70)  # Height of the trunk
    t.right(90)
t.end_fill()

# Move to position for the star at the top
t.penup()
t.goto(-25, 252)  # Adjust position above the tree for the star
t.pendown()

# Set the color to yellow for the star
t.color("yellow")

# Draw the star
draw_star(50)
t.end_fill()


# Hide the turtle and complete the drawing
t.hideturtle()


# Keep the window open
turtle.done()
