from puzzle import Puzzle
from node import Node
import time

# 0) Initialize: Assign starter Puzzle to Node
# 1) Check if node is goal node
#   1a) If goal node, stop! We found solution
#   1b) If not, generate the best next neighbor
# 2) Assign next neighbor to node
# 3) Set neighbor as current node, repeat to 1

#OLD PUZZLES
#initialPuzzle = Puzzle([[0,1,3],[4,2,5],[7,8,6]])
#initialPuzzle = Puzzle([[1,2,3],[0,4,6],[7,5,8]])
#initialPuzzle = Puzzle([[2,8,3],[1,6,4],[7,0,5]]) #Assignment start state

#NEW PUZZLES FOR FINAL PART 2, QUESTION 4
#initialPuzzle = Puzzle([[2,0,5],[1,3,4],[6,7,8]]) #smaller puzzle, part a 
#initialPuzzle = Puzzle([[2,5,4],[1,3,8],[6,7,0]]) #larger puzzle, part a

initialPuzzle = Puzzle([[1,2,6,3],[4,5,7,11],[8,9,10,15],[12,13,14,0]]) #part b, smaller puzzle
#initialPuzzle = Puzzle([[4,1,2,3],[5,6,10,7],[8,9,14,11],[12,0,13,15]]) #part b, different puzzle

initialPuzzle = Puzzle([[1,2,0,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]])

time_start = time.time()
initialNode = Node(initialPuzzle, None, [])
foundSolution = False

currentNode = initialNode
boardsAttempted = 0
print("Start: ")

#start loop!
while(not foundSolution):
    currentNode.printCurrentNode()

    isGoal = currentNode.isGoalNode() #check if our current node is the solution

    if(isGoal): #if so, break out!
        print("Found solution!\n")
        print("Took " + str(boardsAttempted) + " attempts\n")
        currentNode.printCurrentNode()
        
        break

    nextNode = Node(currentNode.getNextNode(), currentNode, []) #next node is the best possible child
    currentNode.assignToChildren(nextNode)

    currentNode = nextNode
    boardsAttempted = boardsAttempted + 1

    #time.sleep(5)

    if(boardsAttempted == 40000):
        print("\nThis board is likely unsolvable!")
        break

time_stop = time.time()
print("Took " + str(time_stop - time_start) + " s")