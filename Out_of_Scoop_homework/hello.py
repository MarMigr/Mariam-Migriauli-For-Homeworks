import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed and position
t.penup()              # Lift the pen so it doesn't draw lines while moving
t.goto(-100,50)           # Move the turtle to the starting position
t.pendown()            # Put the pen down to start writing

# Write the text "Hello"
t.write("Hello", font=("Sylfaen", 50, "italic"))

# Keep the window open
turtle.done()
