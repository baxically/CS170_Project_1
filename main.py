
#Imports
import random as rm

#Variables
validInputs = [1, 2]

firstRow = [0] * 3
secondRow = [0] * 3
thirdRow = [0] * 3

default1 = [3, 1, 2, 6, 4, 5, 0, 7, 8]
default2 = [1, 4, 0, 3, 5, 2, 6, 7, 8]
default3 = [1, 2, 5, 7, 0, 4, 3, 6, 8] 

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

#Main
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
    firstRow = list(map(int, input("Enter your puzzle, use a zero to represent the blank\nEnter the first row, use spaces or tabs between numbers\n").strip().split()))  
    print(firstRow)
    
    #Inputting second row
    secondRow = list(map(int, input("Enter your puzzle, use a zero to represent the blank\nEnter the second row, use spaces or tabs between numbers\n").strip().split()))  
    print(secondRow)
    
    #Inputting third row
    thirdRow = list(map(int, input("Enter your puzzle, use a zero to represent the blank\nEnter the third row, use spaces or tabs between numbers\n").strip().split()))  
    print(thirdRow)
    