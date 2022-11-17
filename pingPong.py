import turtle
import os

A = 0
B = 0

pong = turtle.Screen();
pong.title("PONG")
pong.bgcolor("black")
pong.setup(width=800, height=600)
pong.tracer(0)

# A-Side
padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("white")
padA.penup()
padA.goto(-350, 0)
padA.shapesize(stretch_wid=6, stretch_len=1)

# B-Side
padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("white")
padB.penup()
padB.goto(350, 0)
padB.shapesize(stretch_wid=6, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal") )

# function
def pada_up():
    y = padA.ycor()
    y += 30
    padA.sety(y)


def pada_down():
    y = padA.ycor()
    y -= 30
    padA.sety(y)


def padb_up():
    y = padB.ycor()
    y += 30
    padB.sety(y)


def padb_down():
    y = padB.ycor()
    y -= 30
    padB.sety(y)


pong.listen()
pong.onkeypress(pada_up, "w")
pong.onkeypress(pada_down, "s")
pong.onkeypress(padb_up, "Up")
pong.onkeypress(padb_down, "Down")

# Main
while True:
    pong.update()

    #ballmove
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    #Border
    if padA.ycor() <= -240:
        padA.goto(-350, -240)

    if padB.ycor() <= -240:
        padB.goto(350, -240)

    if padA.ycor() >= 240:
        padA.goto(-350, 240)

    if padB.ycor() >= 240:
        padB.goto(350, 240)

    if ball.ycor() > 290:
        os.system("afplay Sound.wav&")
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        os.system("afplay Sound.wav&")
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dy *= -1
        A += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(A,B), align="center", font=("Courier", 24, "normal") )

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dy *= -1
        B += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(A,B), align="center", font=("Courier", 24, "normal") )


    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padB.ycor() + 60 and ball.ycor() > padB.ycor() - 60):
        os.system("afplay Sound.wav&")
        ball.setx(340)
        ball.dx *= -1
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < padA.ycor() + 60 and ball.ycor() > padA.ycor() - 60):
        os.system("afplay Sound.wav&")
        ball.setx(-340)
        ball.dx *= -1