import sys
from random import randrange

from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout

from client_python.client import Client
from utilities.json_loader import agents_loader, pokemons_loader

Config.set('graphics', 'width', '1100')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.graphics import Line, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock, StringProperty

from Logic.GraphAlgo import GraphAlgo

Builder.load_file('login.kv')

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'


client = Client()
client.start_connection(HOST, PORT)
pokemons_str = client.get_pokemons()
graph_str = client.get_graph()
agents_str = client.get_agents()


class Arena(RelativeLayout):
    login_title = StringProperty("Login")
    login_button_title = StringProperty("Login")

    name_input = None
    case_input = None
    # time_to_end = int(client.time_to_end())

    score_txt = StringProperty()
    time_to_end_txt = StringProperty()
    moves_txt = StringProperty()

    state_game_over = False
    state_game_has_started = False

    sound_begin = None
    sound_music1 = None
    sound_restart = None
    t = 0
    s = 0

    def __init__(self, **kwargs):
        super(Arena, self).__init__(**kwargs)

        self.algo = GraphAlgo()
        self.agents = []  # List
        self.pokemons = pokemons_loader(pokemons_str)  # List
        print(agents_str)
        self.init_stuf()
        self.algo.load_from_json("../../data/A0")
        self.k_nodes = []
        self.k_edges = []
        self.scale_points()
        self.init_audio()
        self.draw_nodes()
        self.draw_edges()
        self.draw_pokemons()
        self.draw_agents()

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def init_stuf(self):
        # self.agents = agents_loader(agents_str)  # List
        # self.pokemons = pokemons_loader(pokemons_str)  # List
        pass

    def init_audio(self):
        self.sound_begin = SoundLoader.load("../../resources/audio/begin.wav")
        self.sound_music1 = SoundLoader.load("../../resources/audio/theme.mp3")
        self.sound_restart = SoundLoader.load("../../resources/audio/restart.wav")

        self.sound_begin.volume = .7
        self.sound_music1.volume = .3
        self.sound_restart.volume = .6

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
        self.unit_x = self.width / (self.max_x - self.min_x) * 0.97
        self.unit_y = self.height / (self.max_y - self.min_y) * 0.96 - 5000

    def draw_nodes(self):
        with self.canvas:
            # Color(0, 0, 0)
            for i in range(0, len(self.algo.graph.nodes)):
                # self.k_nodes.append(Ellipse(source='../../resources/images/pikachu.gif'))
                self.k_nodes.append(Ellipse(source='../../resources/images/pokeball.png'))

    def draw_edges(self):
        with self.canvas:
            Color(0, 0, 0)
            for i in range(0, len(self.algo.graph.edges)):
                self.k_edges.append(Line())

    def update_nodes(self):
        self.scale_points()
        for i, node in enumerate(self.algo.graph.nodes.values()):
            x_scale = (node.pos[0] - self.min_x) * self.unit_x
            y_scale = (node.pos[1] - self.min_y) * self.unit_y

            self.k_nodes[i].pos = x_scale, y_scale
            self.k_nodes[i].size = dp(15), dp(15)

    def update_edges(self):
        self.scale_points()
        for i, key in enumerate(self.algo.graph.edges):
            x1, y1 = (self.algo.graph.nodes.get(key[0]).pos[0] - self.min_x) * self.unit_x + 6, (
                    self.algo.graph.nodes.get(key[0]).pos[1] - self.min_y) * self.unit_y + 6
            x2, y2 = (self.algo.graph.nodes.get(key[1]).pos[0] - self.min_x) * self.unit_x + 6, (
                    self.algo.graph.nodes.get(key[1]).pos[1] - self.min_y) * self.unit_y + 6
            self.k_edges[i].points = [x1, y1, x2, y2]

    def draw_pokemons(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, 1):
                self.pokemons.append(Ellipse(source='../../resources/images/charizard.png'))

    def draw_agents(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, 1):
                self.agents.append(Ellipse(source='../../resources/images/ash2.png'))

    def update_pokemons(self):
        self.scale_points()
        for i in range(0, len(self.pokemons)):
            x, y = randrange(0, self.width), randrange(0, self.height)
            self.pokemons[i].pos = 400, 300
            self.pokemons[i].size = dp(100), dp(100)

    def update_agents(self):
        self.scale_points()
        for i in range(0, len(self.agents)):
            x, y = randrange(0, self.width), randrange(0, self.height)
            self.agents[i].pos = 600, 300
            self.agents[i].size = dp(200), dp(200)

    def update(self, dt):
        # print(client.time_to_end())
        # print(client.get_info())
        # time_factor = dt * 60
        self.update_nodes()
        self.update_edges()
        client.start()
        # print(agents_str)
        # print(pokemons_str)
        # print(self.state_game_has_started)
        # print(self.state_game_over)

        if not self.state_game_over and self.state_game_has_started:
            self.update_agents()
            self.update_pokemons()
            self.t += 1
            self.time_to_end_txt = f"TIME:{str(self.t)}"
            self.score_txt = f"SCORE: {str(self.s)}"
            self.moves_txt = f"MOVES: {str(0)}"

        if self.state_game_over:
            self.t = 0
            self.sb.disabled = True
            self.state_game_has_started = False
            self.state_game_over = True
            self.login_title = "D O N E"
            self.login_button_title = "RESTART"
            self.login_widget.opacity = 1
            self.sound_music1.stop()
            # client.stop_connection()

    def on_login_button_pressed(self, name, case):
        # print("BUTTON")
        self.name_input = name
        self.case_input = case
        print(self.name_input)
        print(self.case_input)
        self.sb = self.ids.stop_button
        self.sb.disabled = True

        if self.state_game_over:
            self.sb.disabled = False
            self.state_game_over = False
            self.sound_restart.play()
            self.sound_music1.play()
            self.state_game_has_started = True
            self.login_widget.opacity = 0
        else:
            self.sb.disabled = False
            self.state_game_over = False
            self.sound_begin.play()
            # self.reset_game()
            self.sound_music1.play()
            self.state_game_has_started = True
            self.login_widget.opacity = 0

    def on_stop_button_pressed(self):
        self.state_game_over = True


class PokemonApp(App):
    pass


if __name__ == '__main__':
    PokemonApp().run()


