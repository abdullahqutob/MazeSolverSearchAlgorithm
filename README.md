# MazeSolverSearchAlgorithm
Search Algorithms in python for solving mazes.

There 3 algorithms are Depth-first Search, Breadth-First Search and Bidirectional-Breadth-First Search.


## How to run

Navigate to the ECM2423 directory in the terminal

type the command that corresponds to the algorithm you'd like to run.

DFS Algorithm: `Python dfs.py`

BFS Algorithm: `Python bfs.py`

Bi-BFS Algorithm: `Python bibfs.py`


You will then be requested to input the maze you would like to search:
Simply type the name of the maze file, including the ".txt" extension



## Custom Mazes

If you would like to include different mazes, add them to the mazes sub-directory.

The maze must meet the following criteria:
- Must be a txt file
- Maze entrance must be on the first line
- Maze exit must be on the last line
- Wall nodes are '#'
- Valid path nodes are '-'


## Results 

The path and corresponding statistics will be printed into the terminal.

The path will also be written into a file in the "Paths" sub-directory, in the form of indexes and letters to describe movements.
