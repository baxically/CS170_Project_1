#Consulted with Noah Allen (nalle005) for logic help

#Imports
import random as rm
import numpy as np  
import time as t   
import heapq as hq
import math 

#Node Class
class node():
    #Initializer
    def __init__(self):
        self.state = []
        self.parent = None
        self.weight = 0
        self.depth = 0
        
    #Overriding < in hq
    def __lt__(self, weight2):
        if self.weight < weight2.weight:
            return True
        else:
            return False
    
    #Overriding > in hq
    def __gt__(self, weight2):
        if self.weight > weight2.weight:
            return True
        else:
            return False
                     
#Variables
validInputs = [1, 2]
algoTypes = [1, 2, 3]

firstRow = [0] * 3
secondRow = [0] * 3
thirdRow = [0] * 3

default1 = [3, 1, 2, 6, 4, 5, 0, 7, 8]
default2 = [1, 4, 0, 3, 5, 2, 6, 7, 8]
default3 = [1, 2, 5, 7, 0, 4, 3, 6, 8] 

goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
initialState = [0] * 9

#Functions
def mapDefaultInput(problem, row1, row2, row3):
    for x in range (0, 3):
        row1[x] = problem[x]
    
    for y in range (0, 3):
        row2[y] = problem[y + 3]
            
    for z in range (0, 3):
        row3[z] = problem[z + 6]   
    
    print(firstRow)
    print(secondRow)
    print(thirdRow)
    
#NOTE: Euclidean distance function from http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
def euclidean(index, val, goal):
    currCol = index % 3
    currRow = index // 3
    goalCol = goal.index(val) % 3
    goalRow = goal.index(val) // 3
    
    x = abs(currCol - goalCol)
    y = abs(currRow - goalRow)
    
    return math.sqrt((x * x) + (y * y))

#Main Driver Code
print("Welcome to 862077930's 8 Puzzle Solver.\n")

#Checks if user input is either 1 or 2
while True:
    userChoice = int(input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n"))
    if userChoice in validInputs:
        #print(userChoice)
        break
    else:
        print("Please enter a valid input.")
        
#If user input is 1, use a default puzzle
if userChoice == 1:
    defaultPuzzle = rm.randint(0, 2)
    if defaultPuzzle == 0:   
        mapDefaultInput(default1, firstRow, secondRow, thirdRow)
    elif defaultPuzzle == 1:
        mapDefaultInput(default2, firstRow, secondRow, thirdRow)
    elif defaultPuzzle == 2:
        mapDefaultInput(default3, firstRow, secondRow, thirdRow)

#If user input is 2, enter their own puzzle
if userChoice == 2:
    #Inputting first row
    #NOTE: Obtained getting array as input method from https://pythonpoint.net/how-to-take-array-input-in-python/
    firstRow = list(map(int, input("Enter your puzzle, use a zero to represent the blank\nEnter the first row, use spaces or tabs between numbers\n").strip().split()))  
    #print(firstRow)
    
    #Inputting second row
    secondRow = list(map(int, input("Enter your puzzle, use a zero to represent the blank\nEnter the second row, use spaces or tabs between numbers\n").strip().split()))  
    #print(secondRow)
    
    #Inputting third row
    thirdRow = list(map(int, input("Enter your puzzle, use a zero to represent the blank\nEnter the third row, use spaces or tabs between numbers\n").strip().split()))  
    #print(thirdRow)

    initialState = np.concatenate((firstRow, secondRow, thirdRow), axis=None)
    print(initialState)
    
#Choosing algorithm
while True:
    algoChoice = int(input("Enter your choice of algorithm\n1- Uniform Cost Search\n2 - A* with Misplaced Tile Heuristic\n3 - A* with Eucledian Distance Heuristic\n"))
    if algoChoice in algoTypes:
        #print(algoChoice)
        break
    else:
        print("Please enter a valid input.")
        
#Uniform Cost Search (Just A* with h(n) = 0)
if algoChoice == 1:
    print("Uniform")
    
#A* with the Misplaced Tile Heuristic 
if algoChoice == 2:
    print("Misplaced")
          
#A* with the Eucledian Distance Heuristic
if algoChoice == 3:
    print("Eucledian")