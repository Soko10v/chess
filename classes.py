class figure:
    def __init__(self, typ, colour, posX, posY):
        self.colour = colour
        self.typ = typ
        self.posX = posX
        self.posY = posY
        # self.type=type

    # type=[1,2,3,4,5,6]
    # 1-pawn
    # 2-knight
    # 3-bishop
    # 4-rook
    # 5-queen
    # 6-king

    def makeblack(self):
        figure.colour = 'B'
        # 0-white
        # 1-black

    #@property
    def getname(self):
        a = self.typ + self.colour
        return a

    @property
    def move(self, int1, int2):
        figure.posX = int1
        figure.posY = int2


class pawn(figure):
    typ = "P"

    def __init__(self, colour, posX, posY):
        self.posX = posX
        self.posY = posY
        self.colour = colour

    name = "P"

    def __delete__(self, instance):
        pass


class knight(figure):
    def __init__(self, clour, posX, posY):
        pass

    def __delete__(self, instance):
        pass


class bishop(figure):
    def __init__(self, clour, posX, posY):
        pass

    def __delete__(self, instance):
        pass


class rook(figure):
    typ = "R"

    def __init__(self, colour, posX, posY):
        self.posX = posX
        self.posY = posY
        self.colour = colour

    name = "R"

    def __delete__(self, instance):
        pass


class queen(figure):
    def __init__(self, clour, posX, posY):
        pass

    def __delete__(self, instance):
        pass


class king(figure):
    def __init__(self, clour, posX, posY):
        pass

    def __delete__(self, instance):
        pass
