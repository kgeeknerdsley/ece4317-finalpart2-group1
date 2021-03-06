import copy

class Puzzle:
    def __init__(self, boardData):
        self.board = boardData #board is a 3x3 array (technically a list, but w/e)

    def getBoard(self):
        return self.board

    #Takes in itself, checks the board, and returns bool if the goal state or not
    #CHANGE THIS TO ADJUST PUZZLE INPUT
    def isGoal(self):
        goalBoard = [[1,2,3],[8,0,4],[7,6,5]] #Assignment goal board!
        goalBoardInorder = [[1,2,3],[4,5,6],[7,8,0]] #inorder goal board
        goalBoardInorder2 = [[0,1,2],[3,4,5],[6,7,8]] #Used for final part 2, question 4
        goalBoardFifteen = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
        goalBoard5x5 = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]

        return self.boardsEqual(goalBoard5x5)

    #Takes in itself, returns list of possible moves to make
    #return type is Puzzle
    def getNeighbors(self):
        neighborBoards = [] #holds all the new boards we make
        holeRow = 0
        holeCol = 0

        #find the hole in our board: DONE
        #check four possible moves: up, down, left, right
        #only calculate the move if we know it's legal

        #iterate over the array. when we find the hole, mark its location!
        for holeSearchR in range(len(self.board)):
            for holeSearchC in range(len(self.board[holeSearchR])):
                if(self.getTile(holeSearchR,holeSearchC) == 0):
                    holeRow = holeSearchR
                    holeCol = holeSearchC

        #print("Hole located at (" + str(holeRow) + " " + str(holeCol) + ")\n")

        #attempt up move
        if(holeRow-1 >= 0):
            tempVal = self.getTile(holeRow-1, holeCol)
            copiedBoard = copy.deepcopy(self.board)
            copiedBoard[holeRow-1][holeCol] = 0
            copiedBoard[holeRow][holeCol] = tempVal
            neighborBoards.append(Puzzle(copiedBoard))
            #print("Attempted up move and added to list")
        
        #attempt left move
        if(holeCol-1 >= 0):
            tempVal = self.getTile(holeRow, holeCol-1)
            copiedBoard = copy.deepcopy(self.board)
            copiedBoard[holeRow][holeCol-1] = 0
            copiedBoard[holeRow][holeCol] = tempVal
            neighborBoards.append(Puzzle(copiedBoard))
            #print("Attempted left move and added to list")

        #attempt right move
        if(holeCol+1 <= 2):
            tempVal = self.getTile(holeRow, holeCol+1)
            copiedBoard = copy.deepcopy(self.board)
            copiedBoard[holeRow][holeCol+1] = 0
            copiedBoard[holeRow][holeCol] = tempVal
            neighborBoards.append(Puzzle(copiedBoard))
            #print("Attempted right move and added to list")

        #attempt down move
        if(holeRow+1 <= 2):
            tempVal = self.getTile(holeRow+1, holeCol)
            copiedBoard = copy.deepcopy(self.board)
            copiedBoard[holeRow+1][holeCol] = 0
            copiedBoard[holeRow][holeCol] = tempVal
            neighborBoards.append(Puzzle(copiedBoard))
            #print("Attempted down move and added to list")

        return neighborBoards

    #return the single neighbor with best hamming score
    #this is priority function!
    def getBestNeighbor(self):
        temp = 999999999
        bestBoard = None

        possibleOptions = self.getNeighbors()
        
        for boardUT in possibleOptions:
            #boardUT.printBoard()
            currentManhattan = boardUT.getManhattanGeneral()
            
            if(temp > currentManhattan):
                temp = currentManhattan
                bestBoard = boardUT
            
        return bestBoard

    #Returns the Hamming code for itself
    def getHamming(self):
        i = 1
        hamming = 0

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(self.board[row][col] != i):
                    hamming = hamming + 1
                elif(row == 2 and col == 2):
                    if(self.board[row][col] != 0):
                        hamming = hamming + 1

                i = i +1
            
        return hamming

    def getManhattan(self):
        i = 1
        manhattan = 0

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):

                #1 case
                if(self.board[row][col] == 1):
                    idealRow = 0
                    idealCol = 1

                    mRow = abs(idealRow - row)
                    mCol = abs(idealCol - col)

                    manhattan = manhattan + mRow + mCol
                    #print("Manhattan for 1 is: " + str(mRow+mCol))

                #2 case
                elif(self.board[row][col] == 2):
                    idealRow = 0
                    idealCol = 2

                    mRow = abs(idealRow - row)
                    mCol = abs(idealCol - col)

                    manhattan = manhattan + mRow + mCol
                    #print("Manhattan for 2 is: " + str(mRow+mCol))

                #3 case
                elif(self.board[row][col] == 3):
                    idealRow = 1
                    idealCol = 0

                    mRow = abs(idealRow - row)
                    mCol = abs(idealCol - col)

                    manhattan = manhattan + mRow + mCol
                    #print("Manhattan for 3 is: " + str(mRow+mCol))

                elif(self.board[row][col] == 4):
                    idealRow = 1
                    idealCol = 1

                    mRow = abs(idealRow - row)
                    mCol = abs(idealCol - col)

                    manhattan = manhattan + mRow + mCol
                    #print("Manhattan for 4 is: " + str(mRow+mCol))

                elif(self.board[row][col] == 5):
                    idealRow = 1
                    idealCol = 2

                    mRow = abs(idealRow - row)
                    mCol = abs(idealCol - col)

                    manhattan = manhattan + mRow + mCol
                    #print("Manhattan for 5 is: " + str(mRow+mCol))

                elif(self.board[row][col] == 6):
                    idealRow = 2
                    idealCol = 0

                    mRow = abs(idealRow - row)
                    mCol = abs(idealCol - col)

                    manhattan = manhattan + mRow + mCol
                    #print("Manhattan for 6 is: " + str(mRow+mCol))

                elif(self.board[row][col] == 7):
                    idealRow = 2
                    idealCol = 1

                    mRow = abs(idealRow - row)
                    mCol = abs(idealCol - col)

                    manhattan = manhattan + mRow + mCol
                    #print("Manhattan for 7 is: " + str(mRow+mCol))

                elif(self.board[row][col] == 8):
                    idealRow = 2
                    idealCol = 2

                    mRow = abs(idealRow - row)
                    mCol = abs(idealCol - col)

                    manhattan = manhattan + mRow + mCol
                    #print("Manhattan for 8 is: " + str(mRow+mCol))

        return manhattan      

    #Expects an inorder board with the hole in (0,0), then increasing across the row
    def getManhattanGeneral(self):
        expected = 0
        manhattan_gen = 0
        found_row = 0
        found_col = 0

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                #print("Looking for " + str(expected) + "'s position, should be at " + str(row) + "," + str(col))

                #find where it's currently located
                for row_search in range(len(self.board)):
                    for col_search in range(len(self.board[row])):
                        value = self.getTile(row_search,col_search) #find the value at a single point in the puzzle

                        if(value == expected): #if the value is what we want, save its location
                            found_row = row_search
                            found_col = col_search
                            #print("Found it at " + str(found_row) + "," + str(found_col))
                
                manhattan_step = abs(found_row-row) + abs(found_col-col)
                #print("Manhattan for " + str(expected) + " is " + str(manhattan_step))

                if(expected == 0):
                    manhattan_gen = manhattan_gen #don't count the 0 or we get stuck in a loop
                else:
                    manhattan_gen = manhattan_gen + abs(found_row - row) + abs(found_col - col)

                expected = expected+1
                #print("Manhattan total so far is " + str(manhattan_gen))
        
        return manhattan_gen

    #Takes in row and column, returns the value at that spot
    def getTile(self,row,col):
        return self.board[row][col]

    #change the tile for the entire board's object (will NOT preserve current board state)
    def changeTile(self, newValue, row, col):
        self.board[row][col] = newValue

    #Takes in a different board, returns true if the same, false otherwise
    def boardsEqual(self, boardToCheck):
        equal = True

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(self.board[row][col] != boardToCheck[row][col]):
                    equal = False

        return equal

    #Prints the board out in text
    def printBoard(self):
        for row in self.board:
            print(row)

    #Returns a coherent string of the board, for mapping purposes
    def printBoardString(self):
        tempString = ""

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                tempString += str(self.board[row][col]) + " "
            tempString += "\n"

        return tempString
    
    def checkIfSolvablePuzzle(self):
        tempString = ""
        inversions = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                tempString += str(self.board[col][row])
        
 
        for i in range(0,len(tempString) - 1):
            for j in range(i,len(tempString) -1):
                if tempString[i] > tempString[j]:
                    inversions += 1

        if (len(tempString) == 16):
            xPos = tempString.find('0')
            if (xPos & 1):
                return not(inversions & 1)
            else:
                return inversions & 1
        else:
            return (inversions % 2 == 0)
