# AI Search Algorithms — Pacman

Implementation of classical search algorithms and search agents in Python, using the UC Berkeley CS188 Pacman educational framework.

This project was completed for **Artificial Intelligence I**. The programming component follows **UC Berkeley CS188 Project 1: Search**. The course assignment also included separate theoretical exercises on search complexity, A* pathfinding on a weighted grid, and bidirectional search; those exercises are not presented here as executable implementations.

## Overview

The project explores how an agent can navigate Pacman mazes by formulating tasks as search problems and selecting appropriate search strategies. It includes uninformed search, cost-sensitive search, heuristic search, and more complex goal formulations involving corners and food collection.

## Implemented Algorithms

| Algorithm | Approach | File |
| --- | --- | --- |
| Depth-First Search (DFS) | Explores deeper states first using a stack | `search.py` |
| Breadth-First Search (BFS) | Explores states in increasing depth using a queue | `search.py` |
| Uniform-Cost Search (UCS) | Expands states according to cumulative path cost | `search.py` |
| A* Search | Combines path cost and a heuristic estimate | `search.py` |

The project also includes work in `searchAgents.py` on search-problem formulations and heuristics, including the **Corners Problem**, **Food Search Problem**, and finding a path to the **closest food dot**.

## Project Structure

```text
.
├── search.py           # Search algorithm implementations
├── searchAgents.py     # Search problems, agents, and heuristics
├── pacman.py           # Pacman application (course framework)
├── game.py             # Game mechanics (course framework)
├── util.py             # Data structures and helpers (course framework)
├── autograder.py       # Educational test runner
├── layouts/            # Pacman maze layouts
├── test_cases/         # Project test cases
└── ...                 # Other supporting framework files
```

## Requirements

- Python 3
- A terminal or command prompt
- The complete Pacman project files, including `layouts/` and `test_cases/`

The original educational framework is designed to run without installing a separate search library.

## Running the Project

From the repository root:

```bash
# Depth-first search
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs

# Breadth-first search
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# Uniform-cost search
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

# A* search with Manhattan distance
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

For a headless run, add `-q` to a command to suppress the graphical display where supported by the framework.

### Automated Tests

The bundled Berkeley-style autograder can be run from the repository root:

```bash
python autograder.py
```

To test an individual question, use the relevant question identifier from the provided test suite, for example:

```bash
python autograder.py -q q1
```

The presence of an autograder does not imply that all tests have been independently verified as passing.

## Concepts Demonstrated

- State-space modeling and graph search
- Stack, queue, and priority-queue frontiers
- Visited-state tracking and path reconstruction
- Cumulative path costs and heuristic evaluation
- Admissible heuristics and multi-goal search problems
- Comparing search strategies on different maze layouts

## Attribution

The Pacman environment, starter code, layouts, and grading infrastructure are derived from the **UC Berkeley CS188 Pacman Projects**. The files changed for this assignment are `search.py` and `searchAgents.py`.

- [UC Berkeley CS188 — Project 1: Search (Fall 2024)](https://inst.eecs.berkeley.edu/~cs188/fa24/projects/proj1/)
