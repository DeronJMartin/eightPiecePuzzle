# Define the distance class for the misplaced tile heuristic
class misplacedTileDist:
    def __init__(self, puzzleSize, puzzleState, goalState):
        self.puzzleSize = puzzleSize
        self.puzzleState = puzzleState
        self.goalState = goalState

    # Define the distance function
    def distance(self):
        distance = 0

        # Iterate through each piece of the current puzzle state and goal state and compare them
        for i in range(self.puzzleSize):
            for j in range(self.puzzleSize):

                # Increment distance if they are not the same
                if (self.goalState[i][j] != self.puzzleState[i][j]):
                    self.distance += 1

        return distance

# Define the generalized manhattan distance class for this type of puzzle
class manhattanTileDistance:
    def __init__(self, puzzleSize, puzzleState, goalState):
        self.puzzleSize = puzzleSize
        self.puzzleState = puzzleState
        self.goalState = goalState

    """
    I didn't bother figuring out an algorithm with less
    time complexity than O(n^^4) for generalizing manhattan distance
    as its still pretty low for puzzle size 2,3,4
    """

    def distance(self):
        distance = 0

        # Iterate through each piece of the goal state
        for i in range(self.puzzleSize):
            for j in range(self.puzzleSize):

                # Iterate through each piece of the current puzzle state
                for ii in range(self.puzzleSize):
                    for jj in range(self.puzzleSize):

                        # Increment distance by distance of puzzle piece to goal piece
                        if (self.goalState[i][j] == self.puzzleState[ii][jj]):
                            distance += (abs(i - ii) + abs(j - jj))
        
        return distance

# Define driver function
def driver(puzzleSize = 3, puzzleState = [[4,8,1],[3,0,5],[7,6,2]], goalState = [[1,2,3],[4,5,6],[7,8,0]]):
    
    # Detect errors in input
    # Detect error in puzzle size
    if (puzzleSize not in [2,3,4]):
        print("This can only solve for 3-piece, 8-piece, or 15-piece puzzles!")
        return -1

    # Detect error in puzzle pieces
    puzzlePieces = set()
    for i in puzzleState:
        for j in i:
            puzzlePieces.add(j)
    correctPuzzlePieces = {range(puzzleSize * puzzleSize - 1)}
    if (puzzlePieces != correctPuzzlePieces):
        print("Error! Incorrect input for puzzle state!")
        return -1

    # Detect error in goal pieces
    goalPieces = set()
    for i in goalState:
        for j in i:
            goalPieces.add(j)
    correctGoalPieces = {range(puzzleSize * puzzleSize - 1)}
    if (goalPieces != correctGoalPieces):
        print("Error! Incorrect input for goal state!")
        return -1


if __name__ == "__main__":
    print("Test")