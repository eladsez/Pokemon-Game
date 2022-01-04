from pokemon import Pokemon
from GraphAlgo import GraphAlgo
from agent import Agent


def compute_next_node(pokemon: Pokemon, algo: GraphAlgo, agent: Agent):
    pok_x = pokemon.pos[0]
    pok_y = pokemon.pos[1]
    pok_on_edge = pokemon.on_edge
    dijkstra_src_node = agent.dest
    if (agent.dest == -1):
        dijkstra_src_node = agent.src
    next_node = algo.shortest_path(dijkstra_src_node, pok_on_edge[0])[1][0]
