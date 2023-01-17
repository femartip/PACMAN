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
from turtle import st

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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    fringe = Stack()                # Fringe to manage which states to expand
    fringe.push(problem.getStartState())
    visited = []                    # List to check whether state has already been visited
    path=[]                         # Final direction list
    pathToCurrent=Stack()           # Stack to maintaing path from start to a state
    currState = fringe.pop()
    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.append(currState)
            successors = problem.getSuccessors(currState)
            for child,direction,cost in successors:
                fringe.push(child)
                tempPath = path + [direction]
                pathToCurrent.push(tempPath)
        currState = fringe.pop()
        path = pathToCurrent.pop()
    return path

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()        #Saves the start state of the problem 

    fringe = util.Queue()
    fringe.push((startState,[],0))
    
    exploredSet = []
    exploredSet.append(startState)

    while not fringe.isEmpty():
        
        node = fringe.pop()
        #print("Nodes: {}".format(node))
        path = node[1]
        if problem.isGoalState(node[0]):
            return path
        else:
            for successor in problem.getSuccessors(node[0]):
                if successor[0] not in exploredSet:
                    fringe.push((successor[0], path + [successor[1]],successor[2]))
                    #print("succesor {}".format(successor))
            exploredSet.append(node[0])
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()            #Saves the start state of the problem 
    
    #Initializing the fringe and closed set    
    fringe = util.PriorityQueue()                   
    fringe.push((startState,[],0),0) #Data structure:((4, 5), ['West'], 1) where the first tuple is the current position, the array is the direction it followed and the number I have no idea   
    
    exploredSet = []                   #Explored nodes
    exploredSet.append(startState)

    while not fringe.isEmpty():             #It always enters to the while 
        
        node = fringe.pop()
        #print("Nodes: {}".format(node))
        path = node[1]

        if problem.isGoalState(node[0]):        #If node is gole, then return the directions it has taken to reach there 
            return path
        
        for successor in problem.getSuccessors(node[0]):        #For all the successor nodes 
            p = path + [successor[1]]
            count = problem.getCostOfActions(p)
            if not successor[0] in exploredSet:           #If succesor node is not already explored
                newSuccessor = (successor[0],node[1]+[successor[1]],count)       
                fringe.push(newSuccessor, count)                   #Saves as the next state the nearest succesor that has not been already explored
        exploredSet.append(node[0])               #Now the current node is already explored 

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
    startState = problem.getStartState()            #Saves the start state of the problem 
    
    
    #Initializing the fringe and closed set    
    fringe = util.PriorityQueue()                   
    fringe.push((startState,[],0),0) #Data structure:((4, 5), ['West'], 1) where the first tuple is the current position, the array is the direction it followed and the number I have no idea   
    
    exploredSet = []                   #Explored nodes
    exploredSet.append(startState)

    while not fringe.isEmpty():             #It always enters to the while 
        
        node = fringe.pop()
        #print("Nodes: {}".format(node))
        path = node[1]

        if problem.isGoalState(node[0]):        #If node is gole, then return the directions it has taken to reach there 
            return path
        
        for successor in problem.getSuccessors(node[0]):        #For all the successor nodes 
            p = path + [successor[1]]
            count = problem.getCostOfActions(p) +  heuristic(successor[0],problem)
            if not successor[0] in exploredSet:           #If succesor node is not already explored
                newSuccessor = (successor[0],node[1]+[successor[1]],count)       
                fringe.push(newSuccessor, count)                   #Saves as the next state the nearest succesor that has not been already explored
        exploredSet.append(node[0])               #Now the current node is already explored 

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
