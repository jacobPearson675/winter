import turtle
import random
screen = turtle.Screen()
screen.screensize(800,800)

screen.bgcolor("gray20")



t_ground = turtle.Turtle()
t_ground.fillcolor("snow2")

t_ground.speed(0)


t_ground.begin_fill()
t_ground.penup()
t_ground.pencolor("snow2")

t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()


#snow
t = turtle.Turtle()
t.speed()
t.speed(0)
t.pensize(5)
for i in range(100):
    t.pencolor('snow')
    x= random.randint(-1000,1000)
    y = random.randint(-100,600)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot()


tree = turtle.Turtle()
tree.speed(0)
tree.pencolor('darkolivegreen')
tree.penup()
tree.goto(-100, -100)
tree.pendown()
tree.begin_fill()
tree.fillcolor("darkolivegreen")
tree.goto(100, -100)
tree.goto(0, 100)
tree.goto(-100, -100)
tree.end_fill()


tree.penup()
tree.goto(-75, 0)
tree.pendown()
tree.begin_fill()
tree.fillcolor("darkolivegreen")
tree.goto(75, 0)
tree.goto(0, 150)
tree.goto(-75, 0)
tree.end_fill()


tree.penup()
tree.goto(-50, 100)
tree.pendown()
tree.begin_fill()
tree.fillcolor("darkolivegreen")
tree.goto(50, 100)
tree.goto(0, 200)
tree.goto(-50, 100)
tree.end_fill()
tree.hideturtle()

o = turtle.Turtle()
o.speed(0)
o.pencolor('red4')
o.fillcolor('red4')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()


o.goto(-15,50)
o.pendown()
o.pencolor('blue4')
o.fillcolor('blue4')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()

o.goto(30,50)
o.pendown()
o.pencolor('blue4')
o.fillcolor('blue4')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()

o.goto(1,95)
o.pendown()
o.pencolor('red4')
o.fillcolor('red4')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()

o.goto(0,-50)
o.pendown()
o.pencolor('goldenrod2')
o.fillcolor('goldenrod2')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()

o.goto(10,135)
o.pendown()
o.pencolor('goldenrod2')
o.fillcolor('goldenrod2')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()

o.goto(-35,-5)
o.pendown()
o.pencolor('goldenrod2')
o.fillcolor('goldenrod2')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()


o.goto(30,-50)
o.pendown()
o.pencolor('blue4')
o.fillcolor('blue4')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()


o.goto(-35,-75)
o.pendown()
o.pencolor('red4')
o.fillcolor('red4')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()

o.goto(-20,125)
o.pendown()
o.pencolor('blue4')
o.fillcolor('blue4')
o.begin_fill()
o.circle(10)
o.end_fill()
o.penup()
o.hideturtle()

s = turtle.Turtle()
s.speed(0)
s.pencolor('gold')
s.fillcolor('gold')
s.begin_fill()
s.penup()
s.goto(0,190)
s.pendown()
s.goto(20,175)
s.goto(15,200)
s.goto(30,215)
s.goto(10,210)
s.penup()
s.goto(0,190)
s.pendown()
s.goto(-20,175)
s.goto(-15,200)
s.goto(-30,215)
s.goto(-10,210)
s.goto(0,235)
s.goto(10,210)
s.goto(0,190)
s.end_fill()
s.hideturtle()


#leftsnowman
snow = turtle.Turtle()
snow.pensize(3)
snow.pencolor('black')
snow.speed(0)
snow.penup()
snow.goto(-200,-200)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(50)
snow.end_fill()
snow.penup()
snow.goto(-200,-100)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(35)
snow.end_fill()
snow.penup()
snow.goto(-200,-30)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(25)
snow.end_fill()


#rightsnowman
snow.penup()
snow.goto(200,-200)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(50)
snow.end_fill()

snow.penup()
snow.goto(200,-100)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(35)
snow.end_fill()

snow.penup()
snow.goto(200,-30)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(25)
snow.end_fill()


#rightsnowmaneyes
snow.penup()
snow.goto(190,0)
snow.pendown()
snow.fillcolor('black')
snow.begin_fill()
snow.circle(3)
snow.end_fill()

snow.penup()
snow.goto(210,0)
snow.pendown()
snow.fillcolor('black')
snow.begin_fill()
snow.circle(3)
snow.end_fill()


#leftsnowmaneyes
snow.penup()
snow.goto(-190,0)
snow.pendown()
snow.fillcolor('black')
snow.begin_fill()
snow.circle(3)
snow.end_fill()

snow.penup()
snow.goto(-210,0)
snow.pendown()
snow.fillcolor('black')
snow.begin_fill()
snow.circle(3)
snow.end_fill()

snow.hideturtle()


#leftsnowmannose
n = turtle.Turtle()
n.speed(0)
n.pencolor('orange')
n.penup()
n.goto(-215, -5)
n.pendown()
n.begin_fill()
n.fillcolor("orange")
n.goto(-187, -5)
n.goto(-186, -5)
n.goto(-203, -15)
n.end_fill()
n.hideturtle()

#rightsnowmannose
n = turtle.Turtle()
n.speed(0)
n.pencolor('orange')
n.penup()
n.goto(215, -5)
n.pendown()
n.begin_fill()
n.fillcolor("orange")
n.goto(187, -5)
n.goto(186, -5)
n.goto(203, -15)
n.end_fill()
n.hideturtle()

#title
w = turtle.Turtle()
w.speed(0)
w.penup()
w.goto(0,300)
w.write(" \"Christmas Chaos\" Made by Jacob Pearson",align = "center", font = ("Arial", 20, 'normal'))
w.hideturtle()


#pond
p = turtle.Turtle()
p.speed(0)
p.penup()
p.goto(-450,-300)
p.pendown()
p.pencolor('slategray2')
p.fillcolor('slategray2')
p.begin_fill()
p.circle(50)
p.end_fill()

p.penup()
p.goto(-420,-260)
p.pendown()
p.pencolor('slategray2')
p.fillcolor('slategray2')
p.begin_fill()
p.circle(50)
p.end_fill()

p.penup()
p.goto(-450,-370)
p.pendown()
p.pencolor('slategray2')
p.fillcolor('slategray2')
p.begin_fill()
p.circle(50)
p.end_fill()

p.penup()
p.goto(-490,-300)
p.pendown()
p.pencolor('slategray2')
p.fillcolor('slategray2')
p.begin_fill()
p.circle(50)
p.end_fill()

p.penup()
p.goto(-390,-350)
p.pendown()
p.pencolor('slategray2')
p.fillcolor('slategray2')
p.begin_fill()
p.circle(50)
p.end_fill()

p.penup()
p.goto(-370,-350)
p.pendown()
p.pencolor('slategray2')
p.fillcolor('slategray2')
p.begin_fill()
p.circle(50)
p.end_fill()

p.penup()
p.goto(-370,-300)
p.pendown()
p.pencolor('slategray2')
p.fillcolor('slategray2')
p.begin_fill()
p.circle(50)
p.end_fill()

p.penup()
p.goto(-360,-310)
p.pendown()
p.pencolor('slategray2')
p.fillcolor('slategray2')
p.begin_fill()
p.circle(50)
p.end_fill()


#moon
m = turtle.Turtle()
m.speed(0)
m.penup()
m.goto(-450,320)
m.pendown()
m.pencolor('gray')
m.fillcolor('gray')
m.begin_fill()
m.circle(70)
m.end_fill()
m.hideturtle()

turtle.done()