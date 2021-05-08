import time
import os
import psutil

#Puzzle to be solved
#puzzle =   [1, 0, 3, 4, 5, 2, 6, 8, 9, 10, 7, 11, 13, 14, 15, 12] # DRDRD  
#puzzle =   [1, 2, 3, 4, 5, 6, 8, 0, 9, 11, 7, 12, 13, 10, 14, 15] # LDLDRR
#puzzle =   [1, 0, 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15] # RDLDDRR
puzzle =   [1, 2, 0, 4, 6, 7, 3, 8, 5, 9, 10, 12, 13, 14, 11, 15] # DLLDRRDR 
#puzzle =   [1, 3, 4, 8, 5, 2, 0, 6, 9, 10, 7, 11, 13, 14, 15, 12] #RULLDRDRD

#Required output for solution
solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0] 

expanded = 0 #variable to calculate the number of expension 

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


#This is the main function and logical where the puzzle is getting solved. 
def Main(puzzle, solution,start):
    LastMove = "Null"
    Moves = "" #variable to store moves made to solve the puzzle
    while(ToBeWorked(puzzle,solution)!=0): #while loop to run the algorithm for solving the puzzle
        currentTime = time.time()
        if(currentTime - start >= 0.5): #Condition to stop infinite loop with time tripper
            print("Over time, problem not solved")
            print("Problem = ", puzzle)
            break
        # Making all the moves and checking how many number are still not matching with the solution
        # Consedering the move in which least number are still not matching with the solution
        # Repeating this in a loop until a solution is found or its 2 minute 

        rValue = lValue = uValue = dValue = 99

        r = MoveRight(puzzle,GetIndex(puzzle)) #Getting the puzzle with the right move 
        if r != [0,0]: #checking if the right move is possible 
            rValue = ToBeWorked(r,solution) #Getting the number of un-match index from the solution index

        l = MoveLeft(puzzle,GetIndex(puzzle)) #Getting the puzzle with Left move 
        if l != [0,0]:  #checking if the left move is possible 
            lValue = ToBeWorked(l,solution) #Getting the number of un-match index from the solution index

        u = MoveUp(puzzle,GetIndex(puzzle)) #Getting the puzzle with Up move
        if u != [0,0]:  #checking if the up move is possible 
            uValue = ToBeWorked(u,solution) #Getting the number of un-match index from the solution index


        d = MoveDown(puzzle,GetIndex(puzzle))#Getting the puzzle with the Down Moe
        if d != [0,0]: #checking if the down move is possible 
            dValue = ToBeWorked(d,solution) #Getting the number of un-match index from the solution index

        # checking for the least number of un-match index condation and going with that solution, with the condition if that move is possible 
        # and also if that move is not reversing our last move.
        if min(rValue,lValue,uValue,dValue) == rValue  and r != [0,0] and LastMove != "L":  #Testing conduction  
            puzzle = r # swaping orignam puzzle with the new condation
            LastMove = "R" 
            Moves = Moves + "R"  # Adding the move to the move String 
        elif min(rValue,lValue,uValue,dValue) == lValue and l != [0,0] and LastMove != "R":  #Testing conduction  
            puzzle = l # swaping orignam puzzle with the new condation
            LastMove = "L"
            Moves = Moves + "L"  # Adding the move to the move String 
        elif min(rValue,lValue,uValue,dValue) == uValue and u != [0,0] and LastMove != "D":  #Testing conduction  
            puzzle = u # swaping orignam puzzle with the new condation
            LastMove = "U"
            Moves = Moves + "U"  # Adding the move to the move String 
        elif min(rValue,lValue,uValue,dValue) == dValue and d != [0,0] and LastMove != "U#":  #Testing conduction  
            puzzle = d # swaping orignam puzzle with the new condation
            LastMove = "D"
            Moves = Moves + "D" # Adding the move to the move String 
        else: #If the condition is not satisfied,  or  infinity loop stopper
            print("Unsolved")
            break
    #printing require output
    print("\n")
    print("Moves : ", Moves)
    print("Expanded: ", expanded)
    print(puzzle)
    

start = time.time() #Noting start time 
process = psutil.Process(os.getpid()) 
MStart = process.memory_info().rss / 1024.0 #Noting starting memoryusage 
Main(puzzle, solution,start) #Calling the main function to solve the puzzle 
end = time.time() #noting the end time
Mend = process.memory_info().rss / 1024.0 #Noting the ned memory state

print("Memory use :", Mend - MStart, " kb")
print(f"Runtime of the program is {end - start}")
print("\n")


