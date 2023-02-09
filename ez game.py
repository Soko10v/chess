from tkinter import *
from tkinter import ttk

from main import *

#visual
root =Tk()
root['bg'] = '#fafafa'
root.title=('basics')
root.geometry('700x450')
root.resizable(width=False, height=False)

frame = Frame(root, bg='grey')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='CHESS', bg="white", font="40")
title.place(relx=0.47,rely=0)

#MOVES
def buff_save (posX, posY):
    global M
    M = 1
    global X
    global Y
    if M==1:
         X=posX
         Y=posY
         M=M+1
    else:
        M=M-1
    return [X,Y]

def MoveFig (x1, x2):
    buff_save(1,6)



##BUTTONS
start = ttk.Button(text="START", command=create_desk())
start.pack(anchor=NW, padx=6, pady=6)
#end = ttk.Button(text="END", command=endgame())
#end.pack(anchor=NW, padx=6, pady=6)

##field
a
a1 = Button(text=a1n, command=MoveFig(1,1), height=1, width=3)
a1.pack(anchor=NW, padx=50, pady=50)

a2 = Button(text=a2n, command=MoveFig(1,2), height=1, width=3)
a2.pack(anchor=NW, padx=50, pady=50)

root.mainloop()