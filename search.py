# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    frontier = Stack()
    visited = set()
    frontier.push((problem.getStartState(), [])) #initialize with starting state an an empty list of actions
    while not (frontier.isEmpty()):
        node, solution = frontier.pop() #we take the first node with the path we have until now
        if problem.isGoalState(node):
            return solution
        visited.add(node) #insert in visited set the node we just expanded
        for suc in problem.getSuccessors(node):
            #if successor is not visited we insert it in the frontier with updated solution (add the action)
            if suc[0] not in visited:    
                frontier.push((suc[0], solution + [suc[1]]))
    return []            
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    frontier = Queue()
    visited = set()
    frontier.push((problem.getStartState(), [])) #initialize with starting state an an empty list of actions
    while not frontier.isEmpty():
        node, solution = frontier.pop() #we take the first node with the path we have until now
        if problem.isGoalState(node):
            return solution
        if node not in visited:
            visited.add(node)
            for state, action, cost in problem.getSuccessors(node):
                frontier.push((state, solution + [action]))

    #if the search end without a solution return an empty list
    return []       
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    frontier = PriorityQueue()
    visited = set()
    frontier.push((problem.getStartState(), [], 0), 0) #initialize with starting state an empty list of actions and cost 0
    while not frontier.isEmpty():
        node, solution, pathcost = frontier.pop() #take the node with the smallest total path cost with the solution path we have until now and its cost
        if problem.isGoalState(node):
            return solution
        if node not in visited:
            visited.add(node)
            for state, action, cost in problem.getSuccessors(node): 
                new_pathcost = pathcost + cost
                if (state not in visited) or (new_pathcost < cost): #if node is not yet visited or if it has better cost, insert it with updated solution and cost
                    frontier.push((state, solution + [action], new_pathcost), new_pathcost)
    return []                

    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"  
    from util import PriorityQueue
    
    frontier = PriorityQueue()
    visited = {}

    start_state = problem.getStartState()
    
    frontier.push((start_state, [], 0), 0)

    while not frontier.isEmpty():
        current_state, actions, current_cost = frontier.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state not in visited or current_cost < visited[current_state]:
            visited[current_state] = current_cost

            for successor, action, step_cost in problem.getSuccessors(current_state):
                new_cost = current_cost + step_cost  
                priority = new_cost + heuristic(successor, problem)
                frontier.push((successor, actions + [action], new_cost), priority)

    return []


    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
