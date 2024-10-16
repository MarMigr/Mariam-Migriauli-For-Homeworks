import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a rhombus
for _ in range(2):
    t.forward(150)  # Draw the first side
    t.left(60)      # Turn 60 degrees for an acute angle
    t.forward(150)  # Draw the second side
    t.left(120)     # Turn 120 degrees for an obtuse angle

# Keep the window open
turtle.done()
