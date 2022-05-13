# Define the distance function for the misplaced tile heuristic
def misplacedTileDist(puzzleSize, puzzleState, goalState):
    distance = 0

    # Iterate through each piece of the current puzzle state and goal state and compare them
    for i in range(puzzleSize):
        for j in range(puzzleSize):

            # Increment distance if they are not the same
            if (goalState[i][j] != puzzleState[i][j]):
                distance += 1

    return distance

# Define the general manhattan distance function for this type of puzzle
def manhattanTileDistance(puzzleSize, puzzleState, goalState):
    distance = 0

    # Iterate through each piece of the goal state
    for i in range(puzzleSize):
        for j in range(puzzleSize):

            # Iterate through each piece of the current puzzle state
            for ii in range(puzzleSize):
                for jj in range(puzzleSize):
                    if (goalState[i][j] == puzzleState[ii][jj]):
                        distance += (abs(i - ii) + abs(j - jj))