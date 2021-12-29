import math
import sys
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '500')

from kivy import platform
from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Line, Quad, Triangle, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import NumericProperty, Clock, ObjectProperty, StringProperty
from kivy.uix.widget import Widget

from algo.Logic.GraphAlgo import GraphAlgo


class Arena(RelativeLayout):
    def __init__(self, **kwargs):
        super(Arena, self).__init__(**kwargs)
        self.algo = GraphAlgo()
        self.agents = []  # List
        self.pokemons = []  # List
        self.algo.load_from_json('../../data/A0.json')
        self.k_nodes = []
        self.k_edges = []
        self.scale_points()
        self.draw_nodes()
        self.draw_edges()

        # Clock.schedule_interval(self.update, 1.0 / 60.0)

    def on_size(self, *args):
        self.update_nodes()
        self.update_edges()

    def scale_points(self):
        self.min_x = self.min_y = sys.float_info.max
        self.max_x = self.max_y = sys.float_info.min
        for i in range(0, len(self.algo.graph.nodes)):
            x = self.algo.graph.nodes[i].pos[0]
            y = self.algo.graph.nodes[i].pos[1]
            self.min_x = min(self.min_x, x)
            self.min_y = min(self.min_y, y)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)
        self.unit_x = self.width / (self.max_x - self.min_x) * 0.96
        self.unit_y = self.height / (self.max_y - self.min_y) * 0.96

    def draw_nodes(self):
        with self.canvas:
            Color(0, 0, 0)
            for i in range(0, len(self.algo.graph.nodes)):
                self.k_nodes.append(Ellipse())

    def draw_edges(self):
        with self.canvas:
            Color(0, 0, 0)
            for i in range(0, len(self.algo.graph.edges)):
                self.k_edges.append(Line())

    def update_nodes(self):
        self.scale_points()
        for i in range(0, len(self.algo.graph.nodes)):
            x, y = self.algo.graph.nodes[i].pos[0], self.algo.graph.nodes[i].pos[1]
            x_scale = (self.algo.graph.nodes[i].pos[0] - self.min_x) * self.unit_x
            y_scale = (self.algo.graph.nodes[i].pos[1] - self.min_y) * self.unit_y

            self.k_nodes[i].pos = x_scale, y_scale
            self.k_nodes[i].size = dp(12), dp(12)

    def update_edges(self):
        self.scale_points()
        for i, key in enumerate(self.algo.graph.edges):
            x1, y1 = (self.algo.graph.nodes.get(key[0]).pos[0] - self.min_x) * self.unit_x + 6, (
                    self.algo.graph.nodes.get(key[0]).pos[1] - self.min_y) * self.unit_y + 6
            x2, y2 = (self.algo.graph.nodes.get(key[1]).pos[0] - self.min_x) * self.unit_x + 6, (
                    self.algo.graph.nodes.get(key[1]).pos[1] - self.min_y) * self.unit_y + 6
            self.k_edges[i].points = [x1, y1, x2, y2]


class PokemonApp(App):
    pass


PokemonApp().run()
