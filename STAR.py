import turtle

#create a canvas
turtle.Screen().bgcolor("purple")

sc=turtle.Screen()
sc.setup(350,620)

turtle.title("SQUARE!!!")

#creating turtle object
t=turtle.Turtle()

#first triangle
t.forward(210)
t.left(120)
t.forward(210)
t.left(120)
t.forward(210)

t.penup()
t.right(150)
t.forward(50)

#secondtriangle
t.pendown()
t.right(90)
t.forward(210)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

turtle.done()