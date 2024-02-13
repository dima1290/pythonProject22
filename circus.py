import turtle
t = turtle.Turtle()
R = 100
print(100/28)
def draw(R1):
    t.color("red")
    t.circle(R1)
    t.penup()
    t.right(90)
    t.forward(R1- R1 / 3.5714285714285716)
    t.pendown()
    t.color("blue")
    t.circle(R1)
    t.right(180)
    t.color("green")
    t.circle(R1)
draw(R)
turtle.done()
