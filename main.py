from classes import *

desk = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]


def create_desk():
    global apw
    apw = pawn("W", 2,2)
    print(apw.getname)



def endgame():
   del apw


create_desk()
#apw.move(3, 4)
#print(apw.posX, apw.posY)
