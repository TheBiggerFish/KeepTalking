
class SolutionInterface:
    def __init__(self):
        pass

class WireSolution:
    def __init__(self,wire):
        self.wire = wire
    def __eq__(self,other):
        return self.wire == other.wire
    def get_wire(self):
        return self.wire