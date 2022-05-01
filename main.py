#Consulted with Noah Allen (nalle005) for logic help

#Imports
import random as rm
import numpy as np  
import time as t   
import heapq as hq
import math 

#Node Class
class Node():
    def __init__(self, state, parent, weight, depth, heuristic, time):
        self.state = state
        self.parent = parent
        #f(n) = g(n) + h(n)
        self.weight = weight #Weight = f(n)
        self.depth = depth #Depth = g(n)
        self.heuristic = heuristic #Heuristic = h(n)
        self.time = time
                     
#Variables
validInputs = [1, 2]
algoTypes = [1, 2, 3]

firstRow = [0] * 3
secondRow = [0] * 3
thirdRow = [0] * 3

default1 = [1, 2, 3, 4, 5, 6, 7, 8, 0] #Trivial Test Case
default2 = [1, 2, 0, 4, 5, 3, 7, 8, 6] #Easy Test Case
default3 = [1, 2, 3, 4, 5, 6, 7, 0, 8] #Very Easy Test Case
default4 = [8, 7, 1, 6, 0, 2, 5, 4, 3] #Oh Boy Test Case
default5 = [0, 1, 2, 4, 5, 3, 7, 8, 6] #Doable Test Case

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
    
    #print(firstRow)
    #print(secondRow)
    #print(thirdRow) 

#NOTE: Euclidean distance function from http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
def euclideanDistance(index, val, goal):
    currCol = index % 3
    currRow = index // 3
    goalCol = goal.index(val) % 3
    goalRow = goal.index(val) // 3
        
    x = abs(currCol - goalCol)
    y = abs(currRow - goalRow)
        
    return math.sqrt((x * x) + (y * y))  

#1 - Uniform Cost Search where h(n) = 0 
#2 - Misplaced Tile; Essentially counts to number of misplaced tiles
#3 - Euclidean; Distance Formula 
def findWeights(heurisitc, node, goal):
    weight = 0
    if heurisitc == 1:
        weight = node.depth
    elif heurisitc == 2:
        count = 0
        for x in range(9):
            if node.state[0] != 1:
                count += 1
            if node.state[1] != 2:
                count += 1
            if node.state[2] != 3:
                count += 1
            if node.state[3] != 4:
                count += 1
            if node.state[4] != 5:
                count += 1
            if node.state[5] != 6:
                count += 1
            if node.state[6] != 7:
                count += 1
            if node.state[7] != 8:
                count += 1
            if node.state[8] != 0:
                count += 1
        weight = node.depth + count
    else:
        temp = 0
        for y in range(9):
            temp = temp + euclideanDistance(y, node.state[y], goal)
        weight = node.depth + temp
    return weight
            
def operators(heuristic, node, goal):
    children = []
    nodeArray = np.array(node.state)
    #print(nodeArray)
    zeroIndex = np.where(nodeArray == 0)[0]
    #print(zeroIndex)
    
    #If blank is index 0
    if zeroIndex[0] == 0:
        #Can move right (to index 1)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[1] = stateCopy[1], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move down (to index 3)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[3] = stateCopy[3], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
    #If blank is index 1
    elif zeroIndex[0] == 1:
        #Can move left (to index 0)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[0] = stateCopy[0], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move right (to index 2)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[2] = stateCopy[2], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move down (to index 4)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[4] = stateCopy[4], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
    #If blank is index 2
    elif zeroIndex[0] == 2:
        #Can move left (to index 1)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[1] = stateCopy[1], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move down (to index 5)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[5] = stateCopy[5], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
    #If blank is index 3
    elif zeroIndex[0] == 3:
        #Can move up (to index 0)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[0] = stateCopy[0], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move right (to index 4)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[4] = stateCopy[4], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move down (to index 6)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[6] = stateCopy[6], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
    #If blank is index 4
    elif zeroIndex[0] == 4:
        #Can move up (to index 1)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[1] = stateCopy[1], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move left (to index 3)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[3] = stateCopy[3], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move right (to index 5)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[5] = stateCopy[5], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move down (to index 7)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[7] = stateCopy[7], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
    #If blank is index 5
    elif zeroIndex[0] == 5:
        #Can move up (to index 2)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[2] = stateCopy[2], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move left (to index 4)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[4] = stateCopy[4], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move down (to index 8)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[8] = stateCopy[8], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
    #If blank is index 6
    elif zeroIndex[0] == 6:
        #Can move up (to index 3)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[3] = stateCopy[3], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move right (to index 7)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[7] = stateCopy[7], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
    #If blank is index 7
    elif zeroIndex[0] == 7:
        #Can move up (to index 4)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[4] = stateCopy[4], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move left (to index 6)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[6] = stateCopy[6], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move right (to index 8)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[8] = stateCopy[8], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
    #If blank is index 8
    elif zeroIndex[0] == 8:
        #Can move up (to index 5)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[5] = stateCopy[5], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
        #Can move left (to index 7)
        stateCopy = node.state.copy()
        stateCopy[zeroIndex[0]], stateCopy[7] = stateCopy[7], stateCopy[zeroIndex[0]]
        children.append(stateCopy)
        
    childrenNodes = []
    
    for child in children:
        tempNode = Node(state = child, parent = node, weight = 0, depth = node.depth + 1, heuristic = heuristic, time = 0) 
        trueWeight = findWeights(heuristic, tempNode, goal)
        newTempNode = Node(state = child, parent = node, weight = trueWeight, depth = node.depth + 1, heuristic = heuristic, time = 0) 
        childrenNodes.append(newTempNode)
    return childrenNodes

def printState(state):
    stateArray = np.array(state)
    print(stateArray)

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
    defaultPuzzle = rm.randint(0, 4)
    if defaultPuzzle == 0:   
        mapDefaultInput(default1, firstRow, secondRow, thirdRow)
        initialState = default1
        print("The Trivial Test Case was randomly chosen\n")
    elif defaultPuzzle == 1:
        mapDefaultInput(default2, firstRow, secondRow, thirdRow)
        initialState = default2
        print("The Easy Test Case was randomly chosen\n")
    elif defaultPuzzle == 2:
        mapDefaultInput(default3, firstRow, secondRow, thirdRow)
        initialState = default3
        print("The Very Easy Test Case was randomly chosen\n")
    elif defaultPuzzle == 3:
        mapDefaultInput(default4, firstRow, secondRow, thirdRow)
        initialState = default4
        print("The Oh Boy Test Case was randomly chosen\n")
    elif defaultPuzzle == 4:
        mapDefaultInput(default5, firstRow, secondRow, thirdRow)
        initialState = default5
        print("The Doable Test Case was randomly chosen\n")

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
    #print(initialState)
    
#Choosing algorithm
initialArray = np.array(initialState)
print(initialArray.reshape(3, 3))
while True:
    algoChoice = int(input("Enter your choice of algorithm\n1- Uniform Cost Search\n2 - A* with Misplaced Tile Heuristic\n3 - A* with Eucledian Distance Heuristic\n"))
    if algoChoice in algoTypes:
        #print(algoChoice)
        break
    else:
        print("Please enter a valid input.")
        
priorQueue = []
numNodesVisited = 0

root = Node(state = initialState, parent = None, weight = 0, depth = 0, heuristic = algoChoice, time = 0)
while len(priorQueue) > 0:
    if root.state == goalState:
        print("Here is the solution:")
        
        if root.parent == None:
            print("The solution was inputted")
            break
        
        #Else Find Solution