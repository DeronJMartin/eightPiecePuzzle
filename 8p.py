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

# Define the generalized manhattan distance function for this type of puzzle
def manhattanTileDistance(puzzleSize, puzzleState, goalState):
    distance = 0

    """
    I didn't bother figuring out an algorithm with less
    time complexity than O(n^^4) for generalizing manhattan distance
    as its still pretty low for puzzle size 2,3,4
    """

    # Iterate through each piece of the goal state
    for i in range(puzzleSize):
        for j in range(puzzleSize):

            # Iterate through each piece of the current puzzle state
            for ii in range(puzzleSize):
                for jj in range(puzzleSize):

                    # Increment distance by distance of puzzle piece to goal piece
                    if (goalState[i][j] == puzzleState[ii][jj]):
                        distance += (abs(i - ii) + abs(j - jj))

# Define driver function
def driver(puzzleSize = 3, puzzleState = [[4,8,1],[3,0,5],[7,6,2]], goalState = [[1,2,3],[4,5,6],[7,8,0]]):
    
    # Detect errors in input
    # Detect error in puzzle size
    if (puzzleSize not in [2,3,4]):
        print("This can only solve for 3-piece, 8-piece, or 15-piece puzzles!")

    # Detect error in puzzle pieces
    puzzlePieces = set()
    for i in puzzleState:
        for j in i:
            puzzlePieces.add(j)
    correctPuzzlePieces = {0, 1, 2, 3, 4, 5, 6, 7, 8}
    if (puzzlePieces != correctPuzzlePieces):
        print("Error! Incorrect input for puzzle state!")

    # Detect error in goal pieces
    goalPieces = set()
    for i in goalState:
        for j in i:
            goalPieces.add(j)
    correctGoalPieces = {0, 1, 2, 3, 4, 5, 6, 7, 8}
    if (goalPieces != correctGoalPieces):
        print("Error! Incorrect input for goal state!")


if __name__ == "__main__":
    print("Test")