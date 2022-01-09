# Pokemon Game

> Made by [Elad Seznayev](https://github.com/eladsez) and [Nerya Bigon](https://github.com/nerya0001).

* Object-Oriented Programming & Design  


![ezgif com-gif-maker](https://user-images.githubusercontent.com/66886354/148678253-33655ea8-e077-4d0f-aa84-3e8548692256.gif)




This assignment is part of OOP course assignments,  
in this assignment we were required to implements all of the knowledge we've learned in this course.  
spesificly, to demonstrate the use of our previous assignments in the course.  
in particular we chose to implement our game on this assignment -  [Weighted directed graphs (directed networks)](https://github.com/nerya0001/Ex3).  

## Introduction
We've designed a Pokemon game, with the purpose to demonstrate the graphs algorithms we've built in our past assignments.  
this game is not an interactive one and it is kind of a simulation more then a game.  
there are 15 cases, each with one of 4 graphs, and a different senario. in each case we've had different number of agent, and thier task was to catch as many pokemons as posibble.  

## Approach
in order to achieve this goal we've used our graphs algorithms in order to find the best path for each agent, in order to maximize the number of pokemons he catchs.  
for evey pokemon that get "eaten" another show up in a random location.  
the simulation end when the time is up (60 sec - 120 sec).  

we had to consider principles like S.O.L.I.D and MVC, and strive towards them in our project architecture.  

In this assignment we've used the Kivy library for the Gui, and our last assignment for the graphs logic and algorithms.  


## The Algorithm:
  * The simulation logic:
    1. place agents initially next to the closest pokemons.   
    2. using Dijkstra's shortest path, find the closest pokemon that wasn't alrady "sold".  
    3. tell the agent where he needs to go according to step 1, and tag the pokemon as "sold".  
    4. after the agent captured the pokemon, reapeat step 1.  
 
 
  * The graphs logic:  
    `shortestPath` - return the shortest path between two nodes.  
    We've implemented the algorithm in the following way:    
      1. Run DIJKSTRA algorithm on the source node - in order to get in each node the shortest path from the source, and the distance. 
      2. Because each node tag "carry" the node that came before it in the path, all there is to do is to loop from the destination node and ask who came before until we get to the source node.
      3. The results are then inserted into a list and returned.  

## Structure
`Ex4_Server_v0.0.jar` - this is the game server, which drive the simulation.    
`client` - This class is in charge of communicating with the server.  
`Arena` - This class is the *"main"* class, in charge of the Gui and calling to the simulation logic.  
`computation.py`- Here is the main logic function of our project - the function that compute the next node for the agent to go to.    
`util` - This class contains helper functions for the logic.  
`DiGraph` - This class represent the graph -> implements the `GraphInterface` interface.  
`GraphAlgo` - this class holds all of the algorithms -> implements the `GraphAlgoInterface` interface.  
`Node` - This class represent a node.  

### dependencies
* [Kivy](https://github.com/kivy/kivy)  


### Screenshots
![l](https://user-images.githubusercontent.com/66886354/148672687-062d8797-cead-462e-b3a3-f334469417b3.png)
![0](https://user-images.githubusercontent.com/66886354/148672693-a1d88e37-ca86-4b00-a246-203fbf71805d.png)
![11](https://user-images.githubusercontent.com/66886354/148672697-a5010cc3-018c-48a5-b47e-9d8fc41828a7.png)



## How To Run
In order to run this program do the following:
1. download the most recent release.  
2. extract the folder.  
3. run the server by opening a terminal in the extracted folder and run the following command:

``` 
java -jar Ex4_Server_v0.0.jar <caseNum(0 - 15)>
```  
4. run the `arena.py` file by openning a terminal in the `Gui` folder which is in the src folder, and run the following command:  

```
python3 arena.py
```  

### More Information
- About Directed, Weighted, and Directed + Weighted graphs: http://math.oxford.emory.edu/site/cs171/directedAndEdgeWeightedGraphs/
- Shortest Path: https://en.wikipedia.org/wiki/Shortest_path_problem#Algorithms
- Dijkstra: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
- Graph Center: https://en.wikipedia.org/wiki/Graph_center
- Travelling Salesman Problem (TSP): https://en.wikipedia.org/wiki/Travelling_salesman_problem
