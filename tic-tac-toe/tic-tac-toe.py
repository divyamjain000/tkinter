from tkinter import *
from os import system
import asyncio
from turtle import TurtleScreen

system('clear')

root=Tk()
root.title("tic-tac-toe")
root.geometry("600x600")
can_wid=Canvas(root,height=400,width=400,bg="black")
can_wid.place(x=50,y=50)
can_wid.create_line(50,150,350,150,fill="white")
can_wid.create_line(50,250,350,250,fill="white")
can_wid.create_line(150,50,150,350,fill="white")
can_wid.create_line(250,50,250,350,fill="white")

def click(event):
    cellno(event.x,event.y)
    # print(event.x,event.y)


can_wid.bind('<Button-1>',click)

turn=FALSE
def cellno(a,b):
    global c
    global d
    if a<150 and a>50:
        c=0
    elif a>150:
        if a<250:
            c=1
        if a>250 and a<350:
            c=2
    if b<150 and b>50:
        d=0
    elif b>150:
        if b<250:
            d=1
        if b>250 and b<350:
            d=2
    game()

def block(r,c):
    return r*3+c



cells=[0,1,2,3,4,5,6,7,8]


def game():
    global turn
    if turn==TRUE and block(c,d) in cells :
        mark(c,d,1)
        cells.remove(block(c,d))
        turn=FALSE
    elif turn==FALSE and block(c,d) in cells:
        mark(c,d,0)
        cells.remove(block(c,d))
        turn=TRUE
# can_wid.bind('<Button-1>',game)
# def win():
#     if


# def winner():


# def gameOver():




def cross(x,y):
    can_wid.create_line(x,y,x+75,y+75,fill="white")
    can_wid.create_line(x+75,y,x,y+75,fill="white")

def zero(x,y):
    can_wid.create_oval(x,y,x+75,y+75)

def mark(a,b,sym):
    if sym==1:
        cross((a+.625)*100,(b+.625)*100)
    elif sym==0:
        zero((a+.625)*100,(b+.625)*100)

exit_btn=Button(root,text="quit",command=root.quit)
exit_btn.place(x=500,y=50)
root.mainloop()