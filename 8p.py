# Import packages
import sys

# Define uniform cost distance which is always zero
class uniformCostDist:
    def distance(self, puzzleSize, puzzleState, goalState):
        return 0

# Define the distance class for the misplaced tile heuristic
class misplacedTileDist:
    def distance(self, puzzleSize, puzzleState, goalState):
        distance = 0

        # Iterate through each piece of the current puzzle state and goal state and compare them
        for i in range(puzzleSize):
            for j in range(puzzleSize):

                # Increment distance if they are not the same
                if (goalState[i][j] != puzzleState[i][j]):
                    distance += 1

        return distance

# Define the generalized manhattan distance class for this type of puzzle
class manhattanTileDistance:

    """
    I didn't bother figuring out an algorithm with less
    time complexity than O(n^^4) for generalizing manhattan
    distance as its still pretty low for puzzle size 2,3,4
    """

    def distance(self, puzzleSize, puzzleState, goalState):
        distance = 0

        # Iterate through each piece of the goal state
        for i in range(puzzleSize):
            for j in range(puzzleSize):

                # Iterate through each piece of the current puzzle state
                for ii in range(puzzleSize):
                    for jj in range(puzzleSize):

                        # Increment distance by distance of puzzle piece to goal piece
                        if (goalState[i][j] == puzzleState[ii][jj]):
                            distance += (abs(i - ii) + abs(j - jj))
        
        return distance

# Define input error detection function
def inputErrorDetection(puzzleSize, puzzleState, goalState):
    # Detect error in puzzle size
    if (puzzleSize not in [2,3,4]):
        sys.exit("This can only solve for 3-piece, 8-piece, or 15-piece puzzles!")

    # Detect error in puzzle pieces
    puzzlePieces = set()
    for i in puzzleState:
        for j in i:
            puzzlePieces.add(j)
    correctPuzzlePieces = set()
    for i in range(puzzleSize * puzzleSize):
        correctPuzzlePieces.add(i)
    if (puzzlePieces != correctPuzzlePieces):
        sys.exit("Error! Incorrect input for puzzle state!")

    # Detect error in goal pieces
    goalPieces = set()
    for i in goalState:
        for j in i:
            goalPieces.add(j)
    correctGoalPieces = set()
    for i in range(puzzleSize * puzzleSize):
        correctGoalPieces.add(i)
    if (goalPieces != correctGoalPieces):
        sys.exit("Error! Incorrect input for goal state!")

# Define MAKE-NODE function
def makeNode(puzzleSize, puzzleState, goalState, cost, heuristic):
    # Calculate heuristic value h(n)
    distance = heuristic.distance(puzzleSize, puzzleState, goalState)

    # Caculate f(n) = g(n) + f(n)
    value = cost + distance

    # Create node of state and f(n)
    node = [puzzleState, value]
    return node

# Define MAKE-QUEUE function
def makeQueue(nodes):
    # Sort nodes by non-decreasing f(n)
    nodes.sort(key = lambda x:x[1])
    return nodes

# Define EMPTY function
def empty(nodes):
    if (len(nodes) == 0):
        return True
    else:
        return False

# Define REMOVE-FRONT function
def removeFront(nodes):
    return nodes.pop(0)

# Define GOAL-TEST
def goalTest(node, goalState):
    if (node[0] == goalState):
        return True
    else:
        return False

# Print puzzle state
def printState(node):
    puzzleState = node[0]
    for i in puzzleState:
        print(i)
    print("\n")

# Define OPERATORS
# The operatots are swapUp, swapRight, swapDown, swapLeft
def swapUp(puzzleSize, puzzleState):
    for i in range(puzzleSize):
        for j in range(puzzleSize):
            if (puzzleState[i][j] == 0):
                puzzleState[i][j] == puzzleState[i-1][j]
                puzzleState[i-1][j] == 0
    return puzzleState

def swapRight(puzzleSize, puzzleState):
    for i in range(puzzleSize):
        for j in range(puzzleSize):
            if (puzzleState[i][j] == 0):
                puzzleState[i][j] == puzzleState[i][j+1]
                puzzleState[i][j+1] == 0
    return puzzleState

def swapDown(puzzleSize, puzzleState):
    for i in range(puzzleSize):
        for j in range(puzzleSize):
            if (puzzleState[i][j] == 0):
                puzzleState[i][j] == puzzleState[i+1][j]
                puzzleState[i+1][j] == 0
    return puzzleState

def swapLeft(puzzleSize, puzzleState):
    for i in range(puzzleSize):
        for j in range(puzzleSize):
            if (puzzleState[i][j] == 0):
                puzzleState[i][j] == puzzleState[i][j+1]
                puzzleState[i][j+1] == 0
    return puzzleState

# Define EXPAND function
def expandState(nodes, node):
    # Calculate puzzle size from puzzle state
    puzzleState = node[0]
    puzzleSize = len(puzzleState[0])
    
    # Initialize variables that indicate which operators are available
    canSwapUp = canSwapRight = canSwapDown = canSwapLeft = True

    # Find blank piece position
    for i in range(puzzleSize):
        for j in range(puzzleSize):
            if (puzzleState[i][j] == 0):
                if (i == 0):
                    canSwapUp = False
                elif (i == puzzleSize-1):
                    canSwapDown = False
                if (j == 0):
                    canSwapLeft = False
                elif (j == puzzleSize-1):
                    canSwapRight = False
                break

    # Add operator puzzle states to queue
    if canSwapUp:
        nodes.append(swapUp(puzzleSize, puzzleState))
    if canSwapRight:
        nodes.append(swapRight(puzzleSize, puzzleState))
    if canSwapDown:
        nodes.append(swapDown(puzzleSize, puzzleState))
    if canSwapLeft:
        nodes.append(swapLeft(puzzleSize, puzzleState))

    return nodes

# Define driver function
# Default puzzleState = [[4,8,1],[3,0,5],[7,6,2]]
def search(puzzleSize = 3, puzzleState = [[1,2,3],[4,5,6],[7,0,8]], goalState = [[1,2,3],[4,5,6],[7,8,0]], algorithm = 3):
    
    # Detect errors in input
    inputErrorDetection(puzzleSize, puzzleState, goalState)

    # Inititalize heuristic to be used
    if (algorithm == 1):
        heuristic = uniformCostDist()
    elif (algorithm == 2):
        heuristic = misplacedTileDist()
    elif (algorithm == 3):
        heuristic = manhattanTileDistance()
    else:
        sys.exit("Error! Incorrect input for algorithm selection!")

    # Initialize queue
    nodes = []

    # Initialize tree depth
    cost = 0

    # Add initial state to queue
    nodes.append(makeNode(puzzleSize, puzzleState, goalState, cost, heuristic))

    # Loop for searching problem space
    while True:

        # Check for failure
        if (empty(nodes)):
            print("Failure! No solution found!")
            break

        # Remove frontier node and print it
        node = removeFront(nodes)
        printState(node)

        # Check for success
        if (goalTest(node, goalState)):
            print("Success! Goal State found!")
            break

        # Expand operators and add new states to queue
        nodes = makeQueue(expandState(nodes, node))

if __name__ == "__main__":
    search()