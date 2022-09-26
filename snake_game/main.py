from tkinter import *
import random


root=Tk()

class game:

    def __init__ (self,parent):
        self.canvas=Canvas(root,height=400,width=400,bg="black")
        self.parent=parent
        self.bx=self.canvas.create_rectangle(20,20,40,40,fill="green")
        self.x=0
        self.y=0
        self.posx=20
        self.posy=40
        self.can()
        self.bind()
        self.genFood()

    def can(self):
        self.parent.geometry("600x600")
        self.canvas.place(x=100,y=100)        
        self.buttons()
        self.head()

    def bind(self):
        self.parent.bind('<Left>',self.left)
        self.parent.bind('<Right>',self.right)
        self.parent.bind('<Up>',self.up)
        self.parent.bind('<Down>',self.down)

    def buttons(self):
        ext_btn=Button(self.parent,text="quit",command=self.parent.quit)
        ext_btn.place(x=475,y=50)

    def head(self):
        self.mve()

        
    def mve(self):

        self.canvas.move(self.bx,self.x,self.y)
        self.posx= self.posx + self.x
        self.posy= self.posy + self.y

        print(self.posx,self.posy)
        self.canvas.after(100,self.mve)

    def right(self,e):
        print(e.keysym)
        self.x=20
        self.y=0

    def left(self,e):
        print(e.keysym)
        self.x=-20
        self.y=0


    def up(self,e):
        print(e.keysym)
        self.x=0
        self.y=-20


    def down(self,e):
        print(e.keysym)
        self.x=0
        self.y=20


    def rnd(self):
        self.m=random.randint(0,19)
        self.n=random.randint(0,19)


    def food(self):
        self.parent.after(250,self.rnd)
        x=20*self.m
        y=20*self.n
        fd=self.canvas.create_rectangle(x,y,x+20,y+20,fill="red")
        if self.isEaten():
            self.destroyFood(fd)

    def genFood(self):
        self.rnd()
        self.food()


    def isEaten(self):
        if self.m==self.posx and self.n==self.posy:
            return True
        else:
            return False
        
    def destroyFood(self,fd):
        self.canvas.delete(fd)

snake=game(root)
root.mainloop()