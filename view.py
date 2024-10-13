# view.py

from turtle import Turtle, Screen
turtle=Turtle()
def setup_screen():
    screen=Screen()
    screen.setup(width=500,height=500)
    screen.title("Ahmad")
    screen.setworldcoordinates(-5,-5,5,5)
    screen.bgcolor("black")

    return screen

def draw_board(turtle,screen):
    turtle.speed(30)
    turtle.pencolor("green")
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3,-1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3,1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

def draw_circle(turtle,x,y,screen):
    turtle.speed(30)
    turtle.up()
    turtle.goto(x,y-0.75)
    turtle.seth(0)
    turtle.color("red")
    turtle.down()
    turtle.circle(0.75,steps=100)
    screen.update()

def draw_x(turtle,x,y,screen):
    turtle.speed(30)
    turtle.color("blue")
    turtle.up()
    turtle.goto(x-0.75,y-0.75)
    turtle.down()
    turtle.goto(x+0.75,y+0.75)
    turtle.up()
    turtle.goto(x-0.75,y+0.75)
    turtle.down()
    turtle.goto(x+0.75,y-0.75)
    screen.update()

def draw_piece(turtle,i,j,p,screen):
    if p==0:
        return 
    x=2*(j-1)
    y=-2*(i-1)
    if p==1:
        draw_x(turtle,x,y,screen)
    else:
        draw_circle(turtle,x,y,screen)


def update_screen(screen):
    screen.update()

