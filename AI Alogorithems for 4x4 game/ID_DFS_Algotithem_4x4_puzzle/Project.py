#Name: Vedant Majmudar
#Class : CS 411
#NetId: vmajmu3
#Project 2 : DFS 4X4 swapping puzzle algorithm with recursive calls


import time
import os
import psutil

#Puzzle to be solved
#puzzle =   [1, 0, 3, 4, 5, 2, 6, 8, 9, 10, 7, 11, 13, 14, 15, 12] # DRDRD  
#puzzle =   [1, 2, 3, 4, 5, 6, 8, 0, 9, 11, 7, 12, 13, 10, 14, 15] # LDLDRR
#puzzle =   [1, 0, 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15] # RDLDDRR
#puzzle =   [1, 2, 0, 4, 6, 7, 3, 8, 5, 9, 10, 12, 13, 14, 11, 15] # DLLDRRDR 
puzzle =   [1, 3, 4, 8, 5, 2, 0, 6, 9, 10, 7, 11, 13, 14, 15, 12] # RULLDRDRD
## >>>> Add more problem with the name as in Line #16 and comment that line


solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0] 
expanded = 0 #variable to calculate the number of expension 
start = time.time() #Noting start time 
process = psutil.Process(os.getpid()) 
MStart = process.memory_info().rss / 1024.0 #Noting starting memoryusage 


#This function take a list as an argument and retrun the index of "0"/empty space in the list.
def GetIndex(puzzle): 
    for i in puzzle: #loop running through the puzzle 
        if puzzle[i] == 0: #checking for index value to be 0
            return i #retruning the index


#This function takes in a list of integers and swaps the 0 to the number on the left
def MoveLeft(puzzle, index):
    if index != 0 and index != 4 and index != 8 and index != 12: #Checking if left move is possible 
        PossibleMove = puzzle.copy() #Making the a copy of puzzle
        PossibleMove[index] = puzzle[index-1] #Swaping the index
        PossibleMove[index-1] = 0 #Swaping the index
        global expanded 
        expanded=1+expanded     #adding the to the expansion
        return PossibleMove     #return the list with moved value 
    return [0,0]


#This function takes in a list of integers and swaps the 0 to the number on the right
def MoveRight(puzzle, index): 
    if index != 3 and index != 7 and index != 11 and index != 15: #Checking if right move is possible 
        PossibleMove = puzzle.copy() #Making the a copy of puzzle
        PossibleMove[index] = puzzle[index+1] #Swaping the index
        PossibleMove[index+1] = 0#Swaping the index
        global expanded
        expanded=1+expanded #adding the to the expansion
        return PossibleMove#return the list with moved value 
    return [0,0]

#This function take in a list of integer and swaps the 0 to the number above it. We need to see it in the form of 4x4 matrix
def MoveUp(puzzle, index):
    if index != 0 and index != 1 and index != 2 and index != 3:#Checking if UP move is possible 
        PossibleMove = puzzle.copy()#Making the a copy of puzzle
        PossibleMove[index] = puzzle[index-4]#Swaping the index
        PossibleMove[index - 4] = 0#Swaping the index
        global expanded
        expanded=1+expanded#adding the to the expansion
        return PossibleMove #return the list with moved value 
    return [0,0]


#This function take in a list of integer and swaps the 0 to the number below it. We need to see it in the form of 4x4 matrix
def MoveDown(puzzle, index):
    if index != 12 and index != 13 and index != 14 and index != 15: #Checking if Down move is possible 
        PossibleMove = puzzle.copy()#Making the a copy of puzzle
        PossibleMove[index] = puzzle[index+4]#Swaping the index
        PossibleMove[index + 4] = 0#Swaping the index
        global expanded
        expanded=1+expanded#adding the to the expansion
        return PossibleMove#return the list with moved value 
    return [0,0]

def ToBeWorked(puzzle, solution): 
    value = 0 #Initiaing with 0 value 
    for i in range (0,16): #running  for the list 
        if(puzzle[i]!=solution[i]):  #Cheking if the value at  both the index matches 
            value=1+value   #Adding to the value 
    return value
#Definning the main function to solve the problem. This function works recursively.
def MainDFS(puzzle,solution,solutionMap, solvedFlag, LastMove, Depth):
    
    # print( solutionMap , " ", Depth)
    
    if(ToBeWorked(puzzle,solution)==0):  #checking if the puzzle has been solved or not, if yes then printing the moves and returning true
        print("######################################################################################")
        print("# \n# PUZZLE SOLVED \n#")
        print( "# Current Puzzle state =", puzzle )
        print( "# Solution Path =", solutionMap )
        return True
    
    # Checking if we are not undoing the last move and then going for the right move.
    # Also, making sure sure if the depth is less then 10 moves. 
    if(LastMove != 'L' and solvedFlag == False and Depth < 10):
        r = MoveRight(puzzle,GetIndex(puzzle)) # getting set of puzzle with right move 
        if(r!=[0,0]): # making sure if the right move is possible or not
            solvedFlag = MainDFS(r ,solution,solutionMap+'R',solvedFlag,'R', Depth+1) #expanding with a recursive call

    # Checking if we are not undoing the last move and then going for the Left move.
    # Also, making sure sure if the depth is less then 10 moves. 
    if(LastMove != 'R' and solvedFlag == False and Depth < 10):
        l = MoveLeft(puzzle,GetIndex(puzzle)) # getting set of puzzle with right move 
        if(l != [0,0]): # making sure if the right move is possible or not
            solvedFlag = MainDFS(l,solution,solutionMap+'L',solvedFlag,'L',Depth+1) #expanding with a recursive call
    

    # Checking if we are not undoing the last move and then going for the UP move.
    # Also, making sure sure if the depth is less then 10 moves. 
    if(LastMove != 'U' and solvedFlag == False and Depth < 10):
        d =  MoveDown(puzzle,GetIndex(puzzle)) # getting set of puzzle with right move 
        if(d != [0,0]): # making sure if the right move is possible or not
            solvedFlag = MainDFS(d,solution,solutionMap+'D',solvedFlag,'D', Depth+1) #expanding with a recursive call
      
    # Checking if we are not undoing the last move and then going for the Down move.
    # Also, making sure sure if the depth is less then 10 moves. 
    if(LastMove != 'D' and solvedFlag == False and Depth < 10):
        u = MoveUp(puzzle,GetIndex(puzzle)) # getting set of puzzle with right move 
        if(u != [0,0]): # making sure if the right move is possible or not
            solvedFlag = MainDFS(u,solution,solutionMap+'U',solvedFlag,'U',Depth+1) #expanding with a recursive call
      
    
    if(solvedFlag == True ): #Going back to initial stack by just returning true and not expanding any more. 
        return True

    return False

    
   
#Calling our main program and biging to start solving the puzzle
# Puzzle == is the question
# solution == is the soultion we need to match our soultion with 
# solutionMap == is the path to solve the puzzle
# solvedFlag == is the flag to make sure if we solve the puzzle or not 
# LastMove == This is to make sure that we are not undoing the last move with the further expension
# Depth == This is to keep track fo the depth of expansion 
MainDFS(puzzle,solution,' ', False,' ',0)

print("# Expanded: ", expanded) #printing number of new nodes expanded 
end = time.time() #noting the end time
Mend = process.memory_info().rss / 1024.0 #Noting the ned memory state
print("# Memory use :", Mend - MStart, " kb") #printing the memory used
print(f"# Runtime of the program is {end - start}") #printing the time taken to solve the puzzle
print("# \n#") 
print("#####################################################################################")