

class Pokemon:
    def __init__(self, value, p_type, pos, on_edge=None):
        self.value = value
        self.type = p_type  # up or down
        self.pos = pos
        self.on_edge = on_edge  # the edge the pokemon is on

    def load(self):
        pass

    def disappear(self):
        pass

    def __repr__(self):
        return f"value:{self.value}, type:{self.type}, pos:{self.pos}"
