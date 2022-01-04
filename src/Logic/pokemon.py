import sys

import numpy as np

from Logic.DiGraph import DiGraph
from Utilities.util import Line, dist


class Pokemon:
    def __init__(self, value, p_type, pos, on_edge=None):
        self.value = value
        self.type = p_type  # up or down
        self.pos = pos
        self.on_edge = on_edge  # the edge the pokemon is on
        self.sold = False

    def which_edge(self, graph: DiGraph):
        min_dist = sys.float_info.max
        for src, dest in graph.edges.keys():
            if src < dest and self.type < 0: continue
            if src > dest and self.type > 0: continue
            src_node = graph.nodes[src]
            dest_node = graph.nodes[dest]
            slope = (src_node.pos[1] - dest_node.pos[1]) / (src_node.pos[0] - dest_node.pos[0])
            line = Line(slope)
            line.findD(src_node.pos[0], src_node.pos[1])
            for x in np.linspace(min(src_node.pos[0], dest_node.pos[0]), max(src_node.pos[0], dest_node.pos[0]), 10):
                y = line.f(x)
                curr_dist = dist(x, y, self.pos[0], self.pos[1])
                if (curr_dist < min_dist):
                    min_dist = curr_dist
                    self.on_edge = (src, dest)

    def __repr__(self):
        return f"value:{self.value}, type:{self.type}, pos:{self.pos}"

    def __eq__(self, other):
        return self.pos == other.pos and self.type == other.type
