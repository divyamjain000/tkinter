from tkinter import * 
import time
import random

root=Tk()
class canvas:
    def __init__(self,parent):
        super().__init__()
        self.makeCanvas(parent,"black",400,400)
    
    def quit_btn(self,parent):
        btn=Button(parent,text="quit",bg="white",command=parent.quit)
        btn.place(x=500,y=50)

    def makeCanvas(self,parent,background,x,y):
        parent.geometry("600x600")
        canvas=Canvas(parent,height=x,width=y,bg=background)
        canvas.place(x=100,y=100)
        self.quit_btn(parent)
        self.head(200,200,canvas,parent)

    def move(self,parent,can_wid,bx):
        can_wid.move(bx,20,0)
        root.after(1000,self.move)

    def head(self,x,y,canvas,parent):
        bx=canvas.create_rectangle(x,y,x+20,y+20,fill="green")
        self.move(parent,canvas,bx)
    def body(self,x,y):
        bd=canvas.create_rectangle(x,y,x+20,y+20,fill="green")
        
    def appendbody(self,a):
        a=1
        
    

    
sketch=canvas(root)

root.mainloop()