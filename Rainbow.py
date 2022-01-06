import turtle
obj=turtle.Turtle()
win=turtle.Screen()

def semi_circle(col, rad, val):
    obj.color(col)
    obj.circle(rad, -180)
    obj.up()
    obj.setpos(vturtle
obj=turtle.Turtle()al, 0)
    obj.down()
    obj.right(180)

col=['violet','indigo','blue','green','yellow','orange','red']

win.bgcolor('black')
obj.right(90)
obj.width(10)
obj.speed(1)

for i in range(7):
    semi_circle(col[i], 10*(i+8), -10*(i+1))
obj.hideturtle()


turtle.done()

