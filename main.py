from classes import *
from array import *

##DESK
desk = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
desk_names = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]


#START/STOP
def create_desk():

    #pawn
    global apw
    apw = pawn("W", 0,1)
    desk[apw.posX][apw.posY]=apw
    #print(apw.getname)

    #field generation
    for i in range  (8):
        for j in range (8):
            try:
                if desk[i][j] != 0:
                    desk_names[i][j] = figure.getname(desk[i][j])
                else:
                    desk_names[i][j] = "  "
            except:
                print("Error desk")
    print("game start")




def endgame():
   del apw

#MOVES
buf=0
#fig=apw
def PeakFig(fig):
    if buf != 0:
        buf=0
    else:
        buf=1
    return buf

def MoveFig (x,y):
    if buf ==0:
       # fig=PeakFig()
        pass

'''
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
'''

##TESTS

#create_desk()
#print(figure.getname(desk[0][1]))
#apw.move(3, 4)
#print(apw.posX, apw.posY)
#create_desk()
try:
    if desk[0][1]!=0:
        a2n=figure.getname(desk[0][1])
    else:
        a1n="  "
    #print(figure.getname(desk[0][1]))
except:
    print("err")