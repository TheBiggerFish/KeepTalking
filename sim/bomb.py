from modules import *
from widgets import *
import random
import string

class Bomb:
    slots = 11

    def __init__(self,num_modules:int,time:int):
        self.modules = Bomb.gen_mods(num_modules)
        if len(self.modules) > Bomb.slots:
            raise Exception("Too many modules on bomb")
        self.strikes = 0
        self.serial = Serial()
        self.timer = Timer(time//60,time%60)

    @staticmethod
    def gen_mods(num_modules:int) -> list:
        modules = []
        for _ in range(num_modules):
            modules.append(WireModule(5))
        return modules

    @staticmethod

    
    def get_module_solution(self,mod_index):
        module = self.modules[mod_index]