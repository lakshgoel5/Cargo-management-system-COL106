from enum import Enum

class Color(Enum):
    BLUE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4
    

class Object:
    def __init__(self, object_id, size=None, color=None):
        self.id = object_id
        self.size=size
        self.capacity=0
        self.color=color
        self.bin_id_appended=None