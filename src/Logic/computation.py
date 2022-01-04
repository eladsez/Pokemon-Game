from pokemon import Pokemon
from GraphAlgo import GraphAlgo
from agent import Agent


def compute_next_node(pokemon: Pokemon, algo: GraphAlgo, agent: Agent) -> int:  # return node_id
    dijkstra_src_node = agent.dest
    if agent.dest == -1:
        dijkstra_src_node = agent.src
    if dijkstra_src_node == pokemon.on_edge[0]:
        return pokemon.on_edge[1]  # the agent is already on the pokemon src node need to go to his dest
    else:
        # the next node is chosen by dijkstra between the agent node to the src of the pokemon edge
        return algo.shortest_path(dijkstra_src_node, pokemon.on_edge[0])[1][0]
