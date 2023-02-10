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


##BUTTONS
start = ttk.Button(text="START", command=lambda: create_desk())
start.pack(anchor=NW, padx=6, pady=6)
#end = ttk.Button(text="END", command=endgame())
#end.pack(anchor=NW, padx=6, pady=6)


##field
try:
    if desk[0][0]!=0:
        a1n=figure.getname(desk[0][0])
    else:
        a1n="  "
except:
    print("Error desk")
a1 = Button(text=desk_names[0][0], command=lambda:MoveFig(0,0), height=1, width=3)
a1.pack(anchor=NW, padx=50, pady=0)

a2 = Button(text=desk_names[0][1], command=MoveFig(0,1), height=1, width=3)
a2.pack(anchor=NW, padx=50, pady=0)

root.mainloop()