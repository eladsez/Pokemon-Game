# Pokemon Game

> Made by [Elad Seznayev](https://github.com/eladsez) and [Nerya Bigon](https://github.com/nerya0001).

* Object-Oriented Programming & Design

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

### dependencies
* [Kivy](https://github.com/kivy/kivy)

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
