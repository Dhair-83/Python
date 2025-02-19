import turtle

#create a canvas
turtle.Screen().bgcolor("purple")

sc=turtle.Screen()
sc.setup(350,620)

turtle.title("SQUARE!!!")

#creating turtle object
t=turtle.Turtle()

#creating a square
t.forward(350)
t.right(90)
t.forward(350)
t.right(90)
t.forward(350)
t.right(90)
t.forward(350)

turtle.done()