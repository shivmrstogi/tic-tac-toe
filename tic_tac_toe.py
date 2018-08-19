from tkinter import *
import tkinter.messagebox

tk=Tk()
tk.title("TIC TAC TOE")
click = True
number=0
count=0

def checker(button):
    
    
    global click
    global number
    global count
    if button["text"] == " " and click == True:
        button["text"] = "X"
        click =False
    elif button["text"] == " " and click == False:
        button["text"] = "O"
        click =True
    if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or
    b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or
    b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or
    b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" or
    b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or
    b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") :
        tkinter.messagebox.showinfo("X won...","congratulatons....X won")
        number=1
    if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or
    b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or
    b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" or
    b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or
    b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or
    b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" or
    b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or
    b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") :
        tkinter.messagebox.showinfo("O won...","congratulatons....O won")
        number=1
    count=count+1
    if count ==9:
        if number!=1:
            tkinter.messagebox.showinfo("MATCH DRAWN..","REPLAY...........")
    
        
        





b1=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b1))
b1.grid(row=0,column=0)

b2=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b2))
b2.grid(row=0,column=1)

b3=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b3))
b3.grid(row=0,column=2)

b4=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b4))
b4.grid(row=1,column=0)

b5=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b5))
b5.grid(row=1,column=1)

b6=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b6))
b6.grid(row=1,column=2)

b7=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b7))
b7.grid(row=2,column=0)

b8=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b8))
b8.grid(row=2,column=1)

b9=Button(tk,text=" ",width=8,height=4,command=lambda:checker(b9))
b9.grid(row=2,column=2)
tk.mainloop()
