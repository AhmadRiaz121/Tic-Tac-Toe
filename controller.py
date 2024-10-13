# controller.py
from turtle import Turtle
from model import create_board, check_winner
from view import setup_screen, draw_board, draw_piece, update_screen
import sys

b=create_board()
turn='x'
screen=setup_screen()
turtle=Turtle()
turtle.hideturtle()

def play(x,y):
    global turn, b
    i=3-int((y+5)/2)
    j=int((x+5)/2)-1
    if i>2 or j>2 or i<0 or j<0 or b[i][j]!=0:
        return
    if turn=='x':
        b[i][j], turn=1, 'o'
    else:
        b[i][j], turn=2, 'x'
    draw_piece(turtle,i,j,b[i][j],screen)
    update_screen(screen)
    winner = check_winner(b)
    if winner==1:
        screen.textinput("Game over!", "X won!")
        sys.exit()
    elif winner==2:
        screen.textinput("Game over!", "O won!")
        sys.exit()
    elif winner==3:
        screen.textinput("Game over!", "Tie!")
        sys.exit()

draw_board(turtle,screen)
screen.onclick(play)
screen.mainloop()
