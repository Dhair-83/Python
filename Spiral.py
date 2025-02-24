import turtle

t=turtle.Turtle()
s=turtle.Screen()

colors=['purple','green','black','indigo','red','blue']

while True:
    for x in range(362):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100+1)
        t.forward(x)
        t.left(60)
    t.right(240)
    for x in range(362,0,-1):
        t.pencolor('black')
        t.width(x/100+7)
        t.forward(x)
        t.right(60)