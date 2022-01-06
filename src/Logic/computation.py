import sys
from typing import List

from Logic.pokemon import Pokemon
from Logic.GraphAlgo import GraphAlgo
from Logic.agent import Agent


def compute_next_node(pokemons: List[Pokemon], algo: GraphAlgo, agent: Agent) -> int:  # return node_id
    min_dist = sys.float_info.max
    chosen_pok = None
    next_node = None
    dijkstra_src_node = agent.dest
    if agent.dest == -1:
        dijkstra_src_node = agent.src

    for pokemon in pokemons:
        if pokemon.sold: continue
        if dijkstra_src_node == pokemon.on_edge[0]:
            return pokemon.on_edge[1]  # the agent is already on the pokemon src node need to go to his dest
        else:
            # the next node is chosen by dijkstra between the agent node to the src of the pokemon edge
            curr_dist, path = algo.shortest_path(dijkstra_src_node, pokemon.on_edge[0])
            if curr_dist < min_dist:
                min_dist = curr_dist
                next_node = path[1]
                chosen_pok = pokemon
    # chosen_pok.sold = True
    return next_node
