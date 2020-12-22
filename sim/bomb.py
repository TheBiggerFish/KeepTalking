from modules import *
from widgets import *
from solution import *
import random

class Bomb:
    slots = 11

    def __init__(self,num_modules:int,minutes:int,seconds:int):
        self.strikes = 0
        self.serial = Serial()
        self.timer = Timer(minutes,seconds)

        if num_modules > Bomb.slots:
            raise Exception("Too many modules on bomb")
        if num_modules < 0:
            raise Exception("Number of bomb modules cannot be negative")
        self.gen_mods(num_modules)

    def gen_mods(self,num_modules:int) -> list:
        self.modules = []
        for _ in range(num_modules):
            # mod_type = random.choice(ModuleType)
            mod_type = ModuleType.WIRE
            if mod_type == ModuleType.WIRE:
                self.modules.append(WireModule.gen_random_module(self.serial))
            elif mod_type == ModuleType.BUTTON:
                pass
            elif mod_type == ModuleType.KEYPAD:
                pass
            elif mod_type == ModuleType.SIMON_SAYS:
                pass
            elif mod_type == ModuleType.WHOS_ON_FIRST:
                pass
            elif mod_type == ModuleType.MEMORY:
                pass
            elif mod_type == ModuleType.MORSE_CODE:
                pass
            elif mod_type == ModuleType.COMPLICATED_WIRES:
                pass
            elif mod_type == ModuleType.WIRE_SEQUENCE:
                pass
            elif mod_type == ModuleType.MAZE:
                pass
            elif mod_type == ModuleType.PASSWORD:
                pass
            elif mod_type == ModuleType.VENTING_GAS:
                pass
            elif mod_type == ModuleType.CAPACITOR_DISCHARGE:
                pass
            elif mod_type == ModuleType.KNOB:
                pass
            else:
                pass

    def get_module(self,mod_index:int) -> ModuleInterface:
        self.check_mod_index(mod_index)
        return self.modules[mod_index]

    def check_mod_index(self,mod_index:int):
        if mod_index >= len(self.modules):
            raise IndexError("Module index out of range")
        if mod_index < 0:
            raise IndexError("Module index cannot be negative")

    def is_solved(self) -> bool:
        for module in self.modules:
            if module.status is not ModuleStatus.SOLVED:
                return False
        return True

    def has_strikes(self, strikes:int):
        if self.strikes >= strikes:
            return True

    def module_action(self,mod_index:int):
        module = self.get_module(mod_index)

        for line in module.get_visual():
            for char in line:
                print(char,end=' ')
            print()

        if module.type == ModuleType.WIRE:
            print(self.serial)
            wire = int(input('Which wire to cut? '))
            correct = module.solve(WireSolution(wire))
            print(correct)
        elif module.type == ModuleType.BUTTON:
            pass
        elif module.type == ModuleType.KEYPAD:
            pass
        elif module.type == ModuleType.SIMON_SAYS:
            pass
        elif module.type == ModuleType.WHOS_ON_FIRST:
            pass
        elif module.type == ModuleType.MEMORY:
            pass
        elif module.type == ModuleType.MORSE_CODE:
            pass
        elif module.type == ModuleType.COMPLICATED_WIRES:
            pass
        elif module.type == ModuleType.WIRE_SEQUENCE:
            pass
        elif module.type == ModuleType.MAZE:
            pass
        elif module.type == ModuleType.PASSWORD:
            pass
        elif module.type == ModuleType.VENTING_GAS:
            pass
        elif module.type == ModuleType.CAPACITOR_DISCHARGE:
            pass
        elif module.type == ModuleType.KNOB:
            pass
        else:
            pass

        if correct:
            module.status = ModuleStatus.SOLVED
        else:
            self.strikes += 1

    def pass_time(self) -> bool:
        return self.timer.step()
