from bomb import Bomb

class Simulation:
    def __init__(self,num_modules:int,time:int):
        self.bomb = Bomb(num_modules,time)

    def pass_time(self) -> bool:
        self.time = max(self.time-1,0)
        return self.time > 0

    def take_action(self):
        pass


