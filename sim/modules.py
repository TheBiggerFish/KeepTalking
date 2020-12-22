from enum import Enum
from widgets import WidgetType
from helpers import *
from solution import *
import random

class ModuleType(Enum):
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
    # IN_PROGESS = 1
    SOLVED = 2

class ModuleInterface:
    def __init__(self):
        self.needy = False
        self.status = ModuleStatus.NOT_STARTED
        self.solution = None
        self.type = None
    
    def get_visual(self):
        return [[' '] * 16] * 16
    
class WireModule(ModuleInterface):
    min_wires = 3
    max_wires = 6

    def __init__(self,num_wires:int,serial:str):
        super().__init__()
        self.type = ModuleType.WIRE
        WireModule.check_wire_count(num_wires)
        self.wires = WireModule.gen_wires(num_wires)
        self.solution = self.find_solution(serial)

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
    
    @staticmethod
    def gen_random_module(serial:str):
        return WireModule(random.randint(WireModule.min_wires,WireModule.max_wires),serial)

    def check_index(self,num:int):
        if num >= len(self.wires):
            raise IndexError("Wire index out of range")
        if num < 0:
            raise IndexError("Wire index cannot be negative")

    @staticmethod
    def check_wire_count(num:int):
        if num > WireModule.max_wires:
            raise Exception("Too many wires for WireModule")
        if num < WireModule.min_wires:
            raise Exception("Not enough wires for WireModule")

    def solve(self,solution:WireSolution) -> bool:
        self.check_index(solution.get_wire())
        wire = self.wires[solution.get_wire()]
        if wire.is_cut():
            return False
        wire.cut()
        return solution == self.solution
    
    def find_solution(self,serial:str) -> WireSolution:
        color = list(map(lambda wire: wire.color, self.wires))
        odd_digit = serial.odd_digit_end()
        if len(color) == 3:
            if color == [Color.BLUE,Color.BLUE,Color.RED]:
                return WireSolution(1)
            if Color.RED not in color:
                return WireSolution(1)
            return WireSolution(2)
        if len(color) == 4:
            if color.count(Color.RED) >= 2 and odd_digit:
                return WireSolution(next(color for color in color[::-1] if color == Color.RED))
            if color[-1] == Color.YELLOW and Color.RED not in color:
                return WireSolution(0)
            if color.count(Color.BLUE) == 1:
                return WireSolution(0)
            if color.count(Color.YELLOW) >= 2:
                return WireSolution(3)
            return WireSolution(1)
        if len(color) == 5:
            if color[-1] == Color.BLACK and odd_digit:
                return WireSolution(3)
            if color.count(Color.YELLOW) >= 2 and color.count(Color.RED) == 1:
                return WireSolution(0)
            if Color.BLACK not in color:
                return WireSolution(1)
            return WireSolution(0)
        if len(color) == 6:
            if Color.YELLOW not in color and odd_digit:
                return WireSolution(2)
            if color.count(Color.YELLOW) == 1 and color.count(Color.WHITE) >= 2:
                return WireSolution(3)
            if Color.RED not in color:
                return WireSolution(5)
            return WireSolution(3)

    def get_visual(self) -> list:
        grid = []
        num_wires = len(self.wires)
        wire_index = 0
        for line in range(16):
            if line in {0,15}:
                grid.append(['.']*16)
            elif line in {2,4,6,9,11,13} and wire_index < num_wires:
                wire = self.wires[wire_index]
                color = Color.letter(wire.color)
                if wire.is_cut():
                    grid.append(['.']*3 + ['#'] + [color]*3 + ['.']*2 + [color]*3 + ['#'] + ['.']*3)
                else:
                    grid.append(['.']*3 + ['#'] + [color]*8 + ['#'] + ['.']*3)
                wire_index += 1
            else:
                grid.append(['.']*3 + ['#'] + ['.']*8 + ['#'] + ['.']*3)
        return grid


        

class ButtonModule(ModuleInterface):
    def __init__(self):
        super().__init__()
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
        super().__init__()
    
class SimonSaysModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class WhosOnFirstModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class MemoryModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class MorseCodeModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class ComplicatedWiresModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class WireSequencesModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class MazeModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class PasswordModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class VentingGasModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class CapacitorDischargeModule(ModuleInterface):
    def __init__(self):
        super().__init__()
    
class KnobModule(ModuleInterface):
    def __init__(self):
        super().__init__()