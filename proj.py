from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import math

board=Tk()
board.title("N-Queens Problem")

buttons={}
a=[]
nq=0
Q={}
img={}
resized={}
my_img={}

def makeGrid(n):
    b=[]
    for i in range(n):
        b.append(1)
    for i in range(n):
        a.append(b)

def onPressed(s,x,y):
    global nq
    buttons[s*x+y+1].destroy()
    img[nq] = Image.open("E:/python 1/bq.png")
    resized[nq] = img[nq].resize((40,50), Image.Resampling.LANCZOS)
    my_img[nq]=ImageTk.PhotoImage(resized[nq])
    Q[nq]=Label(board,image=my_img[nq])
    Q[nq].grid(row=x,column=y)
    if(nq<s):
        if(a[x][y]==1):
            nq+=1
            for i in range(len(a)):
                for j in range(len(a)):
                    if(i==x or j==y or math.fabs(i-x)==math.fabs(j-y)):
                        t=[]
                        for k in range(len(a[i])):
                            if(k==j):
                                t.append(0)
                            else:
                                t.append(a[i][k])
                        a[i]=t
                    if(i==x and j==y):
                        a[i][j]=2
        if(a[x][y]==0):
            print("You Lose")
            messagebox.showerror("Game Over","You Lose")
            nq=s+1
    if(nq==s):
        print("You win")
        messagebox.showinfo("Congratulations","You Won")

def start():
    s=int(size.get()[16:])
    if(s>3):
        makeGrid(s)
        startButton.destroy()
        size.destroy()
        createBoard(s)
    else:
        messagebox.showerror("Invalid size","The entered grid size is invalid.Please enter a valid grid size")

def createButton(color,x,y,s):
    buttons[s*x+y+1]=Button(board,bg=color,height=4,width=7,command=lambda: onPressed(s,x,y))
    buttons[s*x+y+1].grid(row=x,column=y)

def createBoard(n):
    for i in range(n):
        for j in range(n):
            if((i+j)%2==0):
                createButton("black",i,j,n)
            else:
                createButton("white",i,j,n)

size=Entry(board,width=20,border=5)
size.pack()
size.insert(0,"Enter grid size:")

startButton=Button(board,text="START!!!",command=start,fg="white",bg="red")
startButton.pack()

board.mainloop() 
