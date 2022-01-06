import json
from Logic.DiGraph import DiGraph
from Logic.agent import Agent
from Logic.info import Info
from Logic.pokemon import Pokemon
from typing import List



def agents_loader(json_format: str) -> List[Agent]:
    agents_list = []
    json_dict = json.loads(json_format)
    for agent in json_dict["Agents"]:
        pos = agent["Agent"]["pos"].split(",")
        curr_agent = Agent(int(agent["Agent"]["id"]), (float(pos[0]), float(pos[1])), int(agent["Agent"]["src"]),
                           int(agent["Agent"]["dest"]), int(agent["Agent"]["speed"]), float(agent["Agent"]["value"]))
        agents_list.append(curr_agent)
    return agents_list


def pokemons_loader(json_format: str) -> List[Pokemon]:
    pokemons_list = []
    json_dict = json.loads(json_format)
    for pokemon in json_dict["Pokemons"]:
        pos = pokemon["Pokemon"]["pos"].split(",")
        curr_pokemon = Pokemon(float(pokemon["Pokemon"]["value"]), int(pokemon["Pokemon"]["type"]),
                               (float(pos[0]), float(pos[1])))
        pokemons_list.append(curr_pokemon)
    return pokemons_list


def graph_loader(json_format: str) -> DiGraph:
    graph_dict = json.loads(json_format)
    graph = DiGraph()
    for node in graph_dict["Nodes"]:
        pos = tuple(node["pos"].split(","))
        graph.add_node(int(node["id"]), (float(pos[0]), float(pos[1])))
    for edge in graph_dict["Edges"]:
        graph.add_edge(int(edge["src"]), int(edge["dest"]), float(edge["w"]))
    return graph

def info_loader(json_format: str) -> Info:
    json_dict = json.loads(json_format)
    info = None
    for item in json_dict.values():
        info = Info(int(item["pokemons"]), bool(item["is_logged_in"]), int(item["moves"]), int(item["grade"]),
                    int(item["game_level"]),
                    int(item["max_user_level"]), int(item["id"]), item["graph"], int(item["agents"]))
    return info