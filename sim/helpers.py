from enum import Enum

class Color(Enum):
    NONE = 0
    RED = 1
    WHITE = 2
    BLUE = 3
    YELLOW = 4
    BLACK = 5

    @staticmethod
    def letter(color:Enum) -> str:
        if color == Color.BLACK:
            return 'K'
        return color.name[0]

class Label(Enum):
    NONE = 0
    ABORT = 1
    DETONATE = 2
    HOLD = 3
    PRESS = 4

class Wire:
    def __init__(self,color:Color):
        self.color = color
        self.__cut = False
    
    def cut(self):
        if self.__cut:
            raise Exception("Wire already cut")
        self.__cut = True
    
    def is_cut(self) -> bool:
        return self.__cut