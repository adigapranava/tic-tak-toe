import turtle
import numpy
import math
import time
from playsound import playsound

color={'bg':"#99A3A4",  "end_game_b":"#990033", "end_game_f":"#9999CC", "opening_b":"#FFFF00",    "opening_f":"#000000",  "start_b":"#FDFEFE",    "strat_f":"#17202A"}

screen = turtle.Screen()
screen.bgcolor(color["bg"])
screen.setup(580,630) 
t2 = turtle.Turtle()
t2.color("#00E886")
t2.speed(0)
t2.hideturtle()

POSX=-279
POSY=230
SIDE =550 
SIZE=3
NO_OF_CLICKS=1
OLD_NO_OF_CLICKS=0
board=numpy.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
OLD_NO_OF_CLICKS = 0
NO_OF_CLICKS = 1
p1s = "X"
p2s = "O"
turn = 0
row = 4
col = 4


def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagnols(symbol)

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
                if count == 3:
                    break
        if count == 3:
            t2.penup()
            t2.color("red")
            t2.pensize(16)
            t2.goto(POSX + 20, POSY - r * SIDE / SIZE - SIDE /(2* SIZE))
            t2.setheading(0)
            t2.pendown()
            t2.forward(SIDE - 40)
            t2.penup()
            return True
    return False

def check_columns(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
                if count == 3:
                    break
        if count == 3:
            t2.penup()
            t2.color("red")
            t2.pensize(16)
            t2.goto(POSX  + c * SIDE / SIZE + SIDE /(2* SIZE), POSY - 20)
            t2.setheading(-90)
            t2.pendown()
            t2.forward(SIDE - 40)
            t2.penup()
            return True
    return False

def check_diagnols(symbol):
    global t2
    count = 0
    for i in range(3):
        if board[i][i] == symbol:
            count += 1
        if count == 3:
            t2.penup()
            t2.color("#FF00D1")
            t2.pensize(16)
            t2.goto(POSX + 20, POSY- 20)
            t2.setheading(-45)
            t2.pendown()
            t2.forward(SIDE * math.sqrt(2) - 60)
            t2.penup()
            return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        t2.penup()
        t2.color("red")
        t2.pensize(16)
        t2.goto(POSX + 3 * SIDE / SIZE - 20, POSY - 20)
        t2.setheading(225)
        t2.pendown()
        t2.forward(SIDE * math.sqrt(2) - 60)
        t2.penup()
        return True
    else: return False

def layout():
    global POSX, POSY, SIDE
    t1 = turtle.Turtle()

    t1.speed(0)
    t1.hideturtle()
    t1.penup()
    t1.color(color["start_b"])
    t1.pensize(8)
    t1.goto(POSX, POSY)
    t1.pendown()
    t1.begin_fill()
    t1.fillcolor(color["strat_f"])

    for i in range(4):
        t1.forward(SIDE)
        t1.right(90)
    t1.end_fill()

    for j in range(1, SIZE):
        t1.penup()
        t1.color(color["start_b"])
        t1.pensize(4)
        t1.goto(POSX, POSY - j * SIDE / SIZE)
        t1.pendown()
        t1.forward(SIDE)
    t1.right(90)

    for j in range(1, SIZE):
        t1.penup()
        t1.color(color["start_b"])
        t1.pensize(4)
        t1.goto(POSX + j * SIDE / SIZE, POSY)
        t1.pendown()
        t1.forward(SIDE)


    for j in range(1, SIZE):
        t1.penup()
        t1.color("white")
        t1.pensize(4)
        t1.goto(POSX + j * SIDE / SIZE, POSY)
        t1.pendown()
        t1.forward(SIDE)

def cross(i, j):
    global t2
    t2.penup()
    t2.color("#00FFEC")
    t2.goto(POSX + j * SIDE / SIZE + 20, POSY - i * SIDE / SIZE - 20)
    t2.setheading(-45)
    t2.pendown()
    t2.forward(SIDE / SIZE * math.sqrt(2) - 60)
    t2.penup()
    t2.goto(POSX + j * SIDE / SIZE + 20, POSY - (i + 1) * SIDE / SIZE + 20)
    t2.setheading(45)
    t2.pendown()
    t2.forward(SIDE / SIZE * math.sqrt(2) - 60)
    t2.penup()

def circle(i, j):
    global t2
    t2.penup()
    t2.color("#F0FF00")
    t2.goto(POSX + j * SIDE / SIZE + SIDE / SIZE - 40, POSY - i * SIDE / SIZE - SIDE / SIZE + 40)
    t2.pendown()
    t2.circle(SIDE / (2 * SIZE) - 20)


def place(symbol, i, j):
    global board
    board[i][j] = symbol
    if symbol == 'X':
        cross(i, j)
    else:
        circle(i, j)
    print(numpy.matrix(board))

def clicked(x, y):
    row = 3
    col = 3
    global turn,OLD_NO_OF_CLICKS,NO_OF_CLICKS
    for i in range(SIZE):
            for j in range(SIZE):
                if (x >= POSX+j*SIDE/SIZE and x < POSX + (j+1)*SIDE/SIZE) and (y <= POSY-i*SIDE/SIZE and y > POSY - (i+1)*SIDE/SIZE):
                    row = i
                    col = j
    if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row][col] == '-' and turn <= 9 and OLD_NO_OF_CLICKS != NO_OF_CLICKS:
            OLD_NO_OF_CLICKS = NO_OF_CLICKS
            if turn%2 == 0:
                playsound("sounds\clicked.mp3")
                place(p1s, row, col)
                if won(p1s):
                    playsound("sounds\won.mp3")
                    print(p1s,"won")
                    time.sleep(2)
                    quit()
                turn += 1
            else:
                playsound("sounds\clicked.mp3")
                place(p2s, row, col)              
                if won(p2s):
                    playsound("sounds\won.mp3")
                    print(p2s,"won")
                    time.sleep(2)
                    quit()
                turn += 1
            NO_OF_CLICKS += 1
    elif turn == 9:
        if not(won(p1s)) and not(won(p2s)):
            print("Draw")
            quit()
    else:
        print("Error") 
        
def play():
    layout()
    t2.color(color["start_b"])
    t2.pensize(12)
    turtle.listen()
    turtle.onscreenclick(clicked)
    turtle.mainloop()

play()
