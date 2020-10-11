import turtle
import random
n=50
pen=turtle.Turtle()
turtle.Screen().bgcolor("black")
#pen.fillcolor("red")
pen.pensize(2)
colour=["red","white","purple","cyan","blue","green"]

for i in range(n):
    pen.speed(15)
    pen.forward(i*6)     #drawing sides with length i*10
    pen.left(200)   #changing direction anticlockwise with 120 degree
    pen.color(random.choice(colour))    #choose any random colours given above
#turtle.done()


for i in range(n):
    pen.forward(i*4)     #drawing sides with length i*10
    pen.left(144)   #changing direction anticlockwise with 120 degree
    pen.color(random.choice(colour))    #choose any random colours given above
#turtle.done()

for i in range(n):
    pen.forward(i*2)     #drawing sides with length i*10
    pen.left(120)   #changing direction anticlockwise with 120 degree
    pen.color(random.choice(colour))    #choose any random colours given above
turtle.done()