from tkinter import *
from os import system
import asyncio
from tkinter.ttk import Style
from turtle import TurtleScreen

system('clear')

root=Tk()
root.title("tic-tac-toe")
root.geometry("600x600")
can_wid=Canvas(root,height=400,width=400,bg="black")
can_wid.place(x=100,y=100)
can_wid.create_line(50,150,350,150,fill="white",width=3)
can_wid.create_line(50,250,350,250,fill="white",width=3)
can_wid.create_line(150,50,150,350,fill="white",width=3)
can_wid.create_line(250,50,250,350,fill="white",width=3)
label1=Label(root,text=" ")
label1.place(x=225,y=550)
e1=Entry(root)
e1.place(x=50,y=25)
e2=Entry(root)
e2.place(x=400,y=25)
player1=Label(root,text="player 1: ")
player1.place(x=25,y=50)
player2=Label(root,text="player 2:")
player2.place(x=400,y=50)


def start():
    global player1,player2
    print(e1.get())
    player1.config(text="player 1: "+str(e1.get()))
    player2.config(text="player 2: "+str(e2.get()))
    e1.config(state="disabled")
    e2.config(state="disabled")
    
start_btn=Button(root,text="Start game!",command=start).place(x=225,y=50)
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



cells={0:-1,1:-1,2:-1
    ,3:-1,4:-1,5:-1,6:-1,7:-1,8:-1}

def game():
    global label1
    if gameOver()==0:
        
        label1.config(text="winner is: "+ str(e1.get()))
        
    elif gameOver()==1:
        label1.config(text="winner is: "+ str(e2.get()))

    else:
        global turn
        if turn==TRUE and cells[block(c,d)]==-1 and gameOver()==-1 :
            mark(c,d,1)
            cells[block(c,d)]=1
            turn=FALSE
        elif turn==FALSE and cells[block(c,d)]==-1 and gameOver()==-1:
            mark(c,d,0)
            cells[block(c,d)]=0
            turn=TRUE



def gameOver():
    if cells[0]==cells[1]==cells[2]==0 or cells[3]==cells[4]==cells[5]==0 or cells[6]==cells[7]==cells[8]==0 or cells [0]==cells[3]==cells[6]==0 or cells[1]==cells[4]==cells[7]==0 or cells[2]==cells[5]==cells[8]==0 or cells[0]==cells[4]==cells[8]==0 or cells[2]==cells[4]==cells[6]==0:
        return 0
    elif cells[0]==cells[1]==cells[2]==1 or cells[3]==cells[4]==cells[5]==1 or cells[6]==cells[7]==cells[8]==1 or cells [0]==cells[3]==cells[6]==1 or cells[1]==cells[4]==cells[7]==1 or cells[2]==cells[5]==cells[8]==1 or cells[0]==cells[4]==cells[8]==1 or cells[2]==cells[4]==cells[6]==1:
        return 1
    else:
        return -1


def cross(x,y):
    can_wid.create_line(x,y,x+75,y+75,fill="white",width=5,capstyle="round")
    can_wid.create_line(x+75,y,x,y+75,fill="white",width=5,capstyle="round")

def zero(x,y):
    can_wid.create_oval(x,y,x+75,y+75,width=5)

def mark(a,b,sym):
    if sym==1:
        cross((a+.625)*100,(b+.625)*100)
    elif sym==0:
        zero((a+.625)*100,(b+.625)*100)

exit_btn=Button(root,text="quit",command=root.quit)
exit_btn.place(x=500,y=50)
root.mainloop()