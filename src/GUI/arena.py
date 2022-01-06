import sys
import time
from random import randrange

from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout

from Logic.computation import compute_next_node
from client_python.client import Client
from Utilities.json_loader import agents_loader, pokemons_loader, info_loader, graph_loader

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
graph_str = client.get_graph()


# print(client.get_info())


class Arena(RelativeLayout):
    login_title = StringProperty("Login")
    login_button_title = StringProperty("Login")

    ID = None
    # case_input = None
    time_to_end = int(client.time_to_end())

    score_txt = StringProperty()
    time_to_end_txt = StringProperty()
    moves_txt = StringProperty()

    move_count = 0

    total_game_time = time_to_end / 1000
    state_game_over = False
    state_game_has_started = False

    sound_begin = None
    sound_music1 = None
    sound_restart = None

    def __init__(self, **kwargs):
        super(Arena, self).__init__(**kwargs)

        self.algo = GraphAlgo()
        self.algo.graph = graph_loader(client.get_graph())
        self.agents_obj = []  # List
        self.agents = []  # List
        self.pokemons_obj = pokemons_loader(client.get_pokemons())  # List of objects
        self.pokemons = []  # list of ellipse to draw
        self.imageIndex = 0
        for pok in self.pokemons_obj:
            pok.which_edge(self.algo.graph)
            if self.imageIndex % 2 == 0:
                pok.image = '../../resources/images/pikachu.png'
            else:
                pok.image = '../../resources/images/charizard.png'
            self.imageIndex += 1


        self.info = info_loader(client.get_info())

        # adding agents
        if (self.info.num_of_pokemones >= self.info.num_of_agents):
            for i in range(0, self.info.num_of_agents):
                agents_to_add = '{"id":' + f'{self.pokemons_obj[i].on_edge[0]}' + '}'
                client.add_agent(agents_to_add)
        else:
            for i in range(0, self.info.num_of_pokemones):
                agents_to_add = '{"id":' + f'{self.pokemons_obj[i].on_edge[0]}' + '}'
                client.add_agent(agents_to_add)
            for i in range(self.info.num_of_agents - self.info.num_of_pokemones -1, self.info.num_of_agents):
                agents_to_add = '{"id":' + f'{(i + randrange(0, 500, 1)) % self.algo.graph.v_size()}' + '}'
                client.add_agent(agents_to_add)


        self.agents_obj = agents_loader(client.get_agents())

        # self.algo.load_from_json("../../data/A2")
        self.k_nodes = []
        self.k_edges = []

        self.scale_points()
        self.init_audio()
        self.draw_nodes()
        self.draw_edges()
        self.draw_pokemons()
        self.draw_agents()

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def init_audio(self):
        self.sound_begin = SoundLoader.load("../../resources/audio/begin.wav")
        self.sound_music1 = SoundLoader.load("../../resources/audio/theme.mp3")
        self.sound_restart = SoundLoader.load("../../resources/audio/restart.wav")

        self.sound_begin.volume = .0
        self.sound_music1.volume = .0
        self.sound_restart.volume = .0

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
            Color(1, 1, 1)
            for i in range(0, len(self.algo.graph.nodes)):
                self.k_nodes.append(Ellipse(source='../../resources/images/pokeball.png'))

    def draw_edges(self):
        with self.canvas:
            Color(0, 0, 0)
            for i in range(0, len(self.algo.graph.edges)):
                self.k_edges.append(Line())

    def update_nodes(self):
        self.scale_points()
        for i, node in enumerate(self.algo.graph.nodes.values()):
            x, y = (node.pos[0] - self.min_x) * self.unit_x, (node.pos[1] - self.min_y) * self.unit_y
            # print(f'x={x}, y={y}')
            self.k_nodes[i].pos = x, y
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
            for pokemon in self.pokemons_obj:
                # self.pokemons.append(Ellipse())
                self.pokemons.append(Ellipse(source=pokemon.image))


    def draw_agents(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, len(self.agents_obj)):
                self.agents.append(Ellipse(source='../../resources/images/ash.png'))

    def update_pokemons(self):
        self.scale_points()
        for i in range(0, len(self.pokemons_obj)):
            px = self.pokemons_obj[i].pos[0]
            py = self.pokemons_obj[i].pos[1]
            x, y = (px - self.min_x) * self.unit_x, (
                    py - self.min_y) * self.unit_y

            self.pokemons[i].pos = x, y
            self.pokemons[i].size = dp(30), dp(30)

    def update_agents(self):
        self.scale_points()
        for i in range(0, len(self.agents_obj)):
            px = self.agents_obj[i].pos[0]
            py = self.agents_obj[i].pos[1]
            x, y = (px - self.min_x) * self.unit_x, (
                    py - self.min_y) * self.unit_y

            self.agents[i].pos = x, y
            self.agents[i].size = dp(40), dp(40)

    def update(self, dt):
        time_factor = dt * 60
        self.update_nodes()
        self.update_edges()
        self.update_pokemons()
        self.update_agents()

        if not self.state_game_over and self.state_game_has_started and client.is_running():

            self.choose_move()
            self.old_pokemons_obj = self.pokemons_obj
            self.pokemons_obj = pokemons_loader(client.get_pokemons())
            for pok in self.pokemons_obj:
                new_pok = True
                pok.which_edge(self.algo.graph)
                for old_pok in self.old_pokemons_obj:
                    if old_pok == pok:
                        new_pok = False
                        pok.sold = old_pok.sold
                        pok.image = old_pok.image
                if new_pok:
                    if self.imageIndex % 2 == 0:
                        pok.image = '../../resources/images/pikachu.png'
                    else:
                        pok.image = '../../resources/images/charizard.png'
                    self.imageIndex += 1


            self.agents_obj = agents_loader(client.get_agents())
            self.update_agents()
            self.update_pokemons()
            self.info = info_loader(client.get_info())
            self.time_to_end_txt = f"TIME:{str(int(int(client.time_to_end()) / 1000))}"
            self.score_txt = f"SCORE: {str(self.info.grade)}"
            self.moves_txt = f"MOVES: {str(self.info.moves)}"
            self.move_count += 1
            if self.move_count > 5:
                client.move()
                self.move_count = 0

        if self.state_game_over:
            self.sb.disabled = True
            self.state_game_has_started = False
            # self.state_game_over = True
            # self.login_title = "D O N E"
            # self.login_button_title = "RESTART"
            self.login_widget.opacity = 1
            self.sound_music1.stop()
            # client.stop()
            # client.stop_connection()

    def choose_move(self):
        for agent in self.agents_obj:
            # if agent.dest == -1:
            next_node = compute_next_node(self.pokemons_obj, self.algo, agent)
            client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')

    def on_login_button_pressed(self, ID):
        self.ID = ID
        # self.case_input = case
        print(self.ID)
        # print(self.case_input)
        self.sb = self.ids.stop_button
        self.sb.disabled = True
        if ID != "":
            client.log_in(self.ID)
        client.start()

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
        self.sb.disabled = True
        self.state_game_has_started = False
        self.login_widget.opacity = 1
        self.sound_music1.stop()
        client.stop_connection()
        sys.exit()


class PokemonApp(App):
    pass


if __name__ == '__main__':
    PokemonApp().run()
