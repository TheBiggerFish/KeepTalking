from enum import Enum
from sim.widgets import WidgetType
from helpers import *
import random

class ModuleType(Enum):
    NONE = 0
    WIRE = 1
    BUTTON = 2
    KEYPAD = 3
    SIMON_SAYS = 4
    WHOS_ON_FIRST = 5
    MEMORY = 6
    MORSE_CODE = 7
    COMPLICATED_WIRES = 8
    WIRE_SEQUENCE = 9
    MAZE = 10
    PASSWORD = 11
    VENTING_GAS = 12
    CAPACITOR_DISCHARGE = 13
    KNOB = 14

class ModuleStatus(Enum):
    NOT_STARTED = 0
    IN_PROGESS = 1
    SOLVED = 2

class ModuleInterface:
    def __init__(self):
        self.needy = False
        self.state = ModuleStatus.NOT_STARTED
        self.solution = None
        self.type = ModuleType.NONE
    
class WireModule(ModuleInterface):
    min_wires = 3
    max_wires = 6

    def __init__(self,num_wires:int):
        WireModule.check_wire_count(num_wires)
        self.wires = WireModule.gen_wires(num_wires)

    def __str__(self):
        return ','.join(map(lambda wire: wire.color.name + ':' + ('cut' if wire.is_cut() else 'wire'), self.wires))

    @staticmethod
    def gen_wires(num_wires:int) -> list:
        WireModule.check_wire_count(num_wires)
        colors = []
        if num_wires == 3:
            colors = random.choices([Color.RED,Color.WHITE,Color.BLUE],k=3)
        elif num_wires == 4:
            colors = random.choices([Color.RED,Color.WHITE,Color.BLUE,Color.YELLOW],k=4)
        elif num_wires == 5:
            colors = random.choices([Color.RED,Color.WHITE,Color.BLUE,Color.YELLOW,Color.BLACK],k=5)
        elif num_wires == 6:
            colors = random.choices([Color.RED,Color.WHITE,Color.BLUE,Color.YELLOW,Color.BLACK],k=6)

        wires = []
        for color in colors:
            wires.append(Wire(color))
        return wires

    def check_index(self,num:int):
        if num > len(self.wires) or 0 > num:
            raise IndexError("Wire index out of range")

    @staticmethod
    def check_wire_count(num:int):
        if num > WireModule.max_wires:
            raise Exception("Too many wires for WireModule")
        if num < WireModule.min_wires:
            raise Exception("Not enough wires for WireModule")


    def cut_wire(self,index:int,correct:int) -> bool:
        self.check_index(index)
        wire = self.wires[index]
        if wire.is_cut():
            return False
        wire.cut()
        return index == correct
    
    def find_solution(self,serial):
        color = list(map(lambda wire: wire.color, self.wires))
        odd_digit = int(serial[-1]) % 2 == 1
        if len(color) == 3:
            if color == [Color.BLUE,Color.BLUE,Color.RED]:
                return 1
            if Color.RED not in color:
                return 1
            return 2
        if len(color) == 4:
            if color.count(Color.RED) >= 2 and odd_digit:
                return next(color for color in color[::-1] if color == Color.RED)
            if color[-1] == Color.YELLOW and Color.RED not in color:
                return 0
            if color.count(Color.BLUE) == 1:
                return 0
            if color.count(Color.YELLOW) >= 2:
                return 3
            return 1
        if len(color) == 5:
            if color[-1] == Color.BLACK and odd_digit:
                return 3
            if color.count(Color.YELLOW) >= 2 and color.count(Color.RED) == 1:
                return 0
            if Color.BLACK not in color:
                return 1
            return 0
        if len(color) == 6:
            if Color.YELLOW not in color and odd_digit:
                return 2
            if color.count(Color.YELLOW) == 1 and color.count(Color.WHITE) >= 2:
                return 3
            if Color.RED not in color:
                return 5
            return 3
        

class ButtonModule(ModuleInterface):
    def __init__(self):
        self.label = random.choice([Label.ABORT,Label.DETONATE,Label.HOLD,Label.PRESS])
        self.strip = random.choice([Color.BLUE,Color.RED,Color.White,Color.Yellow])
        self.color = random.choice([Color.BLUE,Color.RED,Color.White,Color.Yellow,Color.Black])
        self.held = False

    def tap(self):
        pass

    def hold(self,release:int,time:int):
        pass

    def find_solution(self,batteries,indicators,timer):
        pass

        
    
class KeypadModule(ModuleInterface):
    def __init__(self):
        pass
    
class SimonSaysModule(ModuleInterface):
    def __init__(self):
        pass
    
class WhosOnFirstModule(ModuleInterface):
    def __init__(self):
        pass
    
class MemoryModule(ModuleInterface):
    def __init__(self):
        pass
    
class MorseCodeModule(ModuleInterface):
    def __init__(self):
        pass
    
class ComplicatedWiresModule(ModuleInterface):
    def __init__(self):
        pass
    
class WireSequencesModule(ModuleInterface):
    def __init__(self):
        pass
    
class MazeModule(ModuleInterface):
    def __init__(self):
        pass
    
class PasswordModule(ModuleInterface):
    def __init__(self):
        pass
    
class VentingGasModule(ModuleInterface):
    def __init__(self):
        pass
    
class CapacitorDischargeModule(ModuleInterface):
    def __init__(self):
        pass
    
class KnobModule(ModuleInterface):
    def __init__(self):
        pass