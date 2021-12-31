class Info:
    def __init__(self, num_of_pokemons, is_logged_in, moves, grade, game_level, max_user_level, id, graph,
                 num_of_agents):
        self.num_of_pokemones = num_of_pokemons
        self.is_logged_in = is_logged_in
        self.moves = moves
        self.grade = grade
        self.game_level = game_level
        self.max_user_level = max_user_level
        self.id = id
        self.graph = graph
        self.num_of_agents = num_of_agents

    def __repr__(self):
        return f"pokemons:{self.num_of_pokemones}, is_logged_in:{self.is_logged_in}, moves:{self.moves}, grade:{self.grade}, game_level:{self.game_level}, max_user_level:{self.max_user_level}, id:{self.id}, graph:{self.graph}, agents:{self.num_of_agents}"
