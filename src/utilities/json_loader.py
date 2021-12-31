import json
from Logic.agent import Agent
from Logic.pokemon import Pokemon
from typing import List


def agents_loader(json_format: str) -> List[Agent]:
    agents_list = []
    json_dict = json.loads(json_format)
    curr_agent = None
    pos = None
    for agent in json_dict["Agents"][0].values():
        pos = agent["pos"].split(",")
        curr_agent = Agent(int(agent["id"]), (float(pos[0]), float(pos[1])), int(agent["src"]), int(agent["dest"]),
                           int(agent["speed"]), float(agent["value"]))
        agents_list.append(curr_agent)
    return agents_list


def pokemons_loader(json_format: str) -> List[Pokemon]:
    pokemons_list = []
    json_dict = json.loads(json_format)
    curr_pokemon = None
    pos = None
    for pokemon in json_dict["Pokemons"]:
        pos = pokemon["Pokemon"]["pos"].split(",")
        curr_pokemon = Pokemon(float(pokemon["Pokemon"]["value"]), int(pokemon["Pokemon"]["type"]),
                               (float(pos[0]), float(pos[1])))
        pokemons_list.append(curr_pokemon)
    return pokemons_list


if __name__ == '__main__':
    list = pokemons_loader("""{
        "Pokemons":[
            {
                "Pokemon":{
                "value":5.0,
                "type":-1,
                "pos":"35.20392770907119,32.10833067124629,0.0"
                }
            },
            {
                "Pokemon":{
                "value":8.0,
                "type":-1,
                "pos":"35.20622459040522,32.101281022067994,0.0"
                }
            },
            {
                "Pokemon":{
                "value":13.0,
                "type":-1,
                "pos":"35.21233170626735,32.10466952803471,0.0"
                }
            },
            {
                "Pokemon":{
                "value":5.0,
                "type":-1,
                "pos":"35.21200574506042,32.105721621191464,0.0"
                }
            }
            ]
        }""")
    print(list)
