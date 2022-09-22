from tkinter import * 
import time
import random

root=Tk()
class canvas:
    
    crds={'0':(40,40)}
    def __init__(self,parent):
        makeCanvas(400,400)
        self.parent=parent
    
    def quit_btn(self):
        btn=Button(self.parent,text="quit",bg="white",command=self.parent.quit)
        btn.place(x=500,y=50)

    def head(self):
        x,y=50,50
        bx=self.canvas.create_rectangle(x,y,x+20,y+20,fill="green")

        self.mve(self.parent,canvas,bx)

    def makeCanvas(self,x,y):
        self.parent.geometry("600x600")
        canvas=Canvas(self.parent,height=x,width=y,bg="black")
        canvas.place(x=100,y=100)
        quit_btn()
        head()

    def mve(self,bx):
        for i in range(3):
            self.parent.after(1000, self.can_wid.move(bx,20,0))
        
        # root.after(1000,self.mve(parent,can_wid,bx))

    def body(self,x,y):
        bd=canvas.create_rectangle(x,y,x+20,y+20,fill="green")
        

sketch=canvas(root)

root.mainloop()