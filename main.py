from classes import *
from array import *
#from chess import *

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
    desk[apw.posX][apw.posY]=['P','W',0,1]
    print(apw.getname)

    #field generation
    for i in range  (8):
        for j in range (8):
            try:
                if desk[i][j] != 0:
             #    desk_names[i][j] = figure.getname(figure[desk[i][j][1]][desk[i][j][2]][desk[i][j][3]][desk[i][j][4]])
                   desk_names[i][j]= desk[0][1][i] + desk[0][1][j]
                else:
                    desk_names[i][j] = "  "
            except:
                print("Error desk generation")
    print("game start")
   # print(desk_names[0][1])
    #root.update()
    return "game start"



def endgame():
   del apw

#MOVES
'''buf=0
X=-1
Y=-1
fig=figure(-1,-1,-1,-1)
#fig=apw'''
savedP = figure(-1,-1,-1,-1)
def TookFig (x,y):
    savedP=figure(desk[0][1][0],desk[0][1][1],desk[0][1][2],desk[0][1][3])
def MoveFig (x,y):
    desk [savedP.posY][savedP.posX]=0
    desk_names [savedP.posY][savedP.posX] = "  "
    desk [y][x] = [desk[[savedP.posY][savedP.posX][0],desk[savedP.posY][savedP.posX][1],desk[savedP.posY][savedP.posX][2],desk[savedP.posY][savedP.posX][3]]]


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
'''try:
    if desk[0][1]!=0:
        a2n=figure.getname(desk[0][1])
    else:
        a1n="  "
    #print(figure.getname(desk[0][1]))
except:
    print("err")'''