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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    # visited = set()
    # directions = []

    # def dfs_recur (problem, state, path, isCompleted):
    #     if isCompleted:
    #         return path

    #     if problem.isGoalState(state):
    #         isCompleted = True
    #         print path
    #         return path
        
    #     if state in visited:
    #         return path

    #     visited.add(state)

    #     successors = problem.getSuccessors(state)

    #     for i in range(len(successors)):
    #         if successors[i][0] not in visited:
    #             direction = successors[i][1]
    #             dfs_recur(problem, successors[i][0], path + [direction], isCompleted)

    # directions = dfs_recur(problem, problem.getStartState(), [], False)

    # print(directions)
    # print "Total Count: ", len(directions)
    #util.raiseNotDefined()

    path = []
    start_state = problem.getStartState()
    fringe_list = [(start_state, path)] 
    visited = set()

    while len(fringe_list) != 0: 
        state, current_path = fringe_list.pop()
        if problem.isGoalState(state):
            return current_path
        
        visited.add(state)

        successors = problem.getSuccessors(state)
        
        i = 0
        while i < len(successors):
            if successors[i][0] in visited:
                i += 1
            else:
               fringe_list.append((successors[i][0], current_path + [successors[i][1]]))
               i += 1
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    path = []
    visited = set()
    start_state = problem.getStartState()
    fringe_list = [(start_state, path)]

    visited.add(start_state)

    while len(fringe_list) != 0:

        state, curr_path =fringe_list.pop(0)

        if problem.isGoalState(state):

            return curr_path
        
        successors = problem.getSuccessors(state)

        for next_state, direction, _  in successors:

            if next_state in visited:

                continue
            
            else:

                visited.add(next_state)
                
                fringe_list.append((next_state, curr_path + [direction]))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe_list = util.PriorityQueue()
    visited = set()
    path = []
    start_state = problem.getStartState()

    fringe_list.push((start_state, path, 0), priority=0)

    while not fringe_list.isEmpty():

        curr_state, curr_path, curr_cost = fringe_list.pop()

        if problem.isGoalState(curr_state):

            return curr_path
        
        successors = problem.getSuccessors(curr_state)

        if curr_state not in visited:
            for next_state, direction, cost in successors:
                
                fringe_list.push((next_state, curr_path + [direction], curr_cost + cost), curr_cost + cost)

            visited.add(curr_state)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
