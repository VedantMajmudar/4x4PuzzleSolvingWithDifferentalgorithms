import time
import os
import psutil

print("\n")

#Puzzle to be solved
# puzzle =   [1, 0, 3, 4, 5, 2, 6, 8, 9, 10, 7, 11, 13, 14, 15, 12] # DRDRD  
# puzzle =   [1, 2, 3, 4, 5, 6, 8, 0, 9, 11, 7, 12, 13, 10, 14, 15] # LDLDRR
# puzzle =   [1, 0, 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15] # RDLDDRR
# puzzle =   [1, 2, 0, 4, 6, 7, 3, 8, 5, 9, 10, 12, 13, 14, 11, 15] # DLLDRRDR 
puzzle =   [1, 3, 4, 8, 5, 2, 0, 6, 9, 10, 7, 11, 13, 14, 15, 12] #RULLDRDRD

#Required output for solution
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

#This function takes in the question puzzle and the solved puzzle and retrun the number of unsolved pieces. 
def ToBeWorked(puzzle, solution): 
    value = 0 #Initiaing with 0 value 
    for i in range (0,16): #running  for the list 
        if(puzzle[i]!=solution[i]):  #Cheking if the value at  both the index matches 
            value=1+value   #Adding to the value 
    return value    


def MainAStarMethod(puzzle, solution,flag,solutionMap, Depth,misplaced):

    # print(puzzle," ",Depth, " ", solutionMap[len(solutionMap) -1], " ", solutionMap)

    ValMaps = {}

    rValue = lValue = uValue = dValue = 0

    if(ToBeWorked(puzzle,solution)==0):  #checking if the puzzle has been solved or not, if yes then printing the moves and returning true
        print("######################################################################################")
        print("# \n# PUZZLE SOLVED \n#") 
        print( "# Current Puzzle state =", puzzle ) 
        print( "# Solution Path =", solutionMap )
        print("# Depth (manhattan heuristic)=", Depth)
        print("# Depth (misplaced tiles heuristic)=", misplaced)
        

        return True

    

    l = MoveLeft(puzzle,GetIndex(puzzle)) #Getting the puzzle with Left move 
    if l != [0,0]:  #checking if the left move is possible 
        lValue = ToBeWorked(l,solution) #Getting the number of un-match index from the solution index
        ValMaps[lValue] = l  #Adding misplaced Tile Value and puzzle to dictionaries Data Structure as Ket : Value respectively 

    u = MoveUp(puzzle,GetIndex(puzzle)) #Getting the puzzle with Up move
    if u != [0,0]:  #checking if the up move is possible 
        uValue = ToBeWorked(u,solution) #Getting the number of un-match index from the solution index
        ValMaps[uValue] = u #Adding misplaced Tile Value and puzzle to dictionaries Data Structure as Ket : Value respectively 
    
    d = MoveDown(puzzle,GetIndex(puzzle))#Getting the puzzle with the Down Moe
    if d != [0,0]: #checking if the down move is possible 
        dValue = ToBeWorked(d,solution) #Getting the number of un-match index from the solution index
        ValMaps[dValue] = d #Adding misplaced Tile Value and puzzle to dictionaries Data Structure as Ket : Value respectively 

    r = MoveRight(puzzle,GetIndex(puzzle)) #Getting the puzzle with the right move 
    if r != [0,0]: #checking if the right move is possible 
        rValue = ToBeWorked(r,solution) #Getting the number of un-match index from the solution index
        ValMaps[rValue] = r #Adding misplaced Tile Value and puzzle to dictionaries Data Structure as Ket : Value respectively 

    #(3:[] ,7[]. 9[])
    # for i in sorted (ValMaps) : 
    #     print(i , "  ", ValMaps[i])

    for i in sorted (ValMaps) : #Using a for loop to go through the list dictionaries  in sorted order and calling MainAStarMethod function to solve it recursively 
        if Depth < 10: #Making sure we do not do on the wrong path more then 10 depths
            if i == rValue and solutionMap[len(solutionMap) -1] != "L": #Checking if we are not stuck in r and l or u and d loop 
                #print(ValMaps[i]," ",Depth, " ", solutionMap[len(solutionMap) -1], " ", solutionMap)
                flag = MainAStarMethod(ValMaps[i], solution,flag,solutionMap+"R", Depth+1,i+misplaced) #recursive call

            elif i == uValue and solutionMap[len(solutionMap) -1] != "D": #Checking if we are not stuck in r and l or u and d loop 
                # print(ValMaps[i]," ",Depth, " ", solutionMap[len(solutionMap) -1], " ", solutionMap)
                flag = MainAStarMethod(ValMaps[i], solution,flag,solutionMap+"U",Depth+1,i+misplaced) #recursive call
               
            elif i == dValue and solutionMap[len(solutionMap) -1] != "U": #Checking if we are not stuck in r and l or u and d loop 
                # print(ValMaps[i]," ",Depth, " ", solutionMap[len(solutionMap) -1], " ", solutionMap)
                flag = MainAStarMethod(ValMaps[i], solution,flag,solutionMap+"D",Depth+1,i+misplaced) #recursive call
               

            elif i == lValue and solutionMap[len(solutionMap) -1] != "R": #Checking if we are not stuck in r and l or u and d loop 
                # print(ValMaps[i]," ",Depth, " ", solutionMap[len(solutionMap) -1], " ", solutionMap)
                flag = MainAStarMethod(ValMaps[i], solution,flag,solutionMap+"L",Depth+1,i+misplaced) #recursive call
                

        if flag == True: #Making sure if the problem is not already salved
            return True #if it is solved the retuning true flags to get ot of the recursive call 
    return False #Retrung false to the previous recursive call


lol = MainAStarMethod(puzzle,solution, False, " ", 1,0) #inteating to solve the problem 

print("# Expanded: ", expanded) #printing number of new nodes expanded 
end = time.time() #noting the end time
Mend = process.memory_info().rss / 1024.0 #Noting the ned memory state
print("# Memory use :", Mend - MStart, " kb") #printing the memory used
print(f"# Runtime of the program is {end - start}") #printing the time taken to solve the puzzle
print("# \n#") 
print("#####################################################################################")
