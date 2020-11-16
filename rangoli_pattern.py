import turtle

s = turtle.Screen()
s.bgcolor("black")

turtle.speed(0)

c = 0
d = 0

while True:
    for i in ["red","yellow","red","yellow"]:
        turtle.pencolor(i)
        turtle.forward(80)
        turtle.right(90)
    turtle.right(15)    
    c += 1
    if c>390/15:
        turtle.forward(50)
        c = 0
        d += 1
        if d>=12:
         break
        
        
turtle.hideturtle() 
turtle.done()