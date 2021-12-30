

class Agent:
    def __init__(self, id, pos, src, dest, speed, value):
        self.id = id
        self.pos = pos
        self.src = src
        self.dest = dest
        self.speed = speed
        self.value = value

    def move(self):
        pass

    def catch(self):
        pass

    def __repr__(self) -> str:
        return f"id:{self.id}, pos:{self.pos}, src:{self.src}, dest:{self.dest}, speed:{self.speed}, value:{self.value}"


