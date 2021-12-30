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
        curr_agent = Agent(agent["id"], (pos[0], pos[1]), agent["src"], agent["dest"], agent["speed"], agent["value"])
        agents_list.append(curr_agent)
    return agents_list


def pokemons_loader(json_format: str) -> List[Pokemon]:
    pokemons_list = []
    json_dict = json.loads(json_format)
    curr_pokemon = None
    pos = None
    for pokemon in json_dict["Pokemons"][0].values():
        pos = pokemon["pos"].split(",")
        curr_pokemon = Pokemon(pokemon["value"], pokemon["type"], (pos[0], pos[1]))
        pokemons_list.append(curr_pokemon)
    return pokemons_list





if __name__ == '__main__':
    list = pokemons_loader("""{
            "Pokemons":[
                {
                    "Pokemon":{
                        "value":5.0,
                        "type":-1,
                        "pos":"35.197656770719604,32.10191878639921,0.0"
                    }
                }
            ]
        }""")
    print(list)
