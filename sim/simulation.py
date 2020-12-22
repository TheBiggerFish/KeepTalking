from bomb import Bomb

class Simulation:
    def __init__(self,num_modules:int,minutes:int=0,seconds:int=0):
        self.bomb = Bomb(num_modules,minutes,seconds)

    def pass_time(self) -> bool:
        if self.bomb.is_solved():
            return False
        if self.bomb.has_strikes(3):
            return False
        return self.bomb.pass_time()

    def take_action(self,module_index):
        self.bomb.module_action(module_index)

