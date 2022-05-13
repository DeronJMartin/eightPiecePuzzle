# Define the distance function for the misplaced tile heuristic
def misplacedTileDist(puzzleSize, puzzleState, goalState):
    distance = 0

    # Go through each piece of the current state and goal state and compare them
    # Increment distance if they are not the same
    for i in range(puzzleSize):
        for j in range(puzzleSize):
            if (goalState[i][j] != puzzleState[i][j]):
                distance += 1

    return distance
import math
import matplotlib.pyplot as plt

def misplacedTileDist(puzzleSize, puzzleState, goalState):
    n = puzzleSize
    
