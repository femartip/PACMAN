# PACMAN
Pacman agent for autonomous playing created in Python. Three different implementations: Search, Logic/Game Search and Reinforcement Learning.
To see all possible commands: python pacman.py -h

## 1. Search
BFS - python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
UCS - python pacman.py -l bigMaze -p SearchAgent -a fn=bfs
A* - python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

## 2. MultiAgent
Reflex agent - python pacman.py -p ReflexAgent
Minimax -  python pacman.py -p MinimaxAgent -k 1
Alpha-beta - python pacman.py -p AlphaBetaAgent -a depth=3
Expectimax - python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3

## 3. Reinforcement Learning
Q-Learning - python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
ApproximateQLearning(using features of map) - python pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid

