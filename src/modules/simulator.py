# -- coding: utf-8 --
"""
Algorithm to simulate the spreading of fire in a forest.

@author: Evelyn Paiz
"""

# ----------------------------------------------------------
# Imports
from modules.parser import *                                # Parsing of the parameters
from modules.grid import *                                  # Grid helper functions
from modules.color import getColoredText                    # Color for the printed text
import random                                               # Random number generation
import os.path                                              # Path management
# ----------------------------------------------------------
# States of a node in the forest grid
STATES = {
    "normal": {"code": 0, "color": {"r": 50, "g": 205, "b": 50}, "symbol": "\u25a6"},
    "fire": {"code": 1, "color": {"r": 255, "g": 0, "b": 0}, "symbol": "\u25a3"},
    "burned": {"code": 2, "color": {"r": 176, "g": 196, "b": 222}, "symbol": "\u25a1"}
}
# ----------------------------------------------------------

def getNodeKeyFromCode(code):
    for key in STATES: 
        if(STATES[key]["code"] == code):
            return key

def simulateFire(file):
    """
    simulateFire function runs a simulation of the spreading of
    fire in a forest grid.

    :param file: file containing the input parameters
    """

    # Input parameters are parsed from input file
    ext = os.path.splitext(file)[-1].lower()

    if(ext == ".txt"): params = parseText(file)
    elif(ext == ".json"): params = parseJSON(file)
    else:
        print(getColoredText(255, 0, 0, "File extension not supported, please enter a .txt or .json file"))
        exit()

    # Initial variables
    w = params["widthGrid"]                                 # Width of the forest grid
    h = params["heightGrid"]                                # Height of the forest grid
    pThreshold = params["burningProbability"]               # Probability threshold
    initFire = params["initFire"]                           # Initial fire set of positions

    NORMAL = STATES["normal"]["code"]                       # States of the forest coded
    FIRE = STATES["fire"]["code"]
    BURNED = STATES["burned"]["code"]

    forest = [[NORMAL for x in range(w)] for y in range(h)] # Forest grid of size wxh
    nodePos = [[i, j] for i in range(h) for j in range(w)]  # All coordinates in the forest grid 
    t = 0                                                   # Number of steps in the simulation

    # The fire starts in the fores at t = 0
    for x in range(len(initFire)):
        # Check that each index is correctly defined as [i, j],
        # if not print the error
        try:
            # Init the fire in each corresponding node
            forest[initFire[x][0]][initFire[x][1]] = FIRE           
        except Exception as e:
            print(getColoredText(255, 0, 0, 'Input parameters not properly defined, please check'))
            exit()

    # Color the forest grid
    coloredForest = [[None for x in range(w)] for y in range(h)]
    for i in range(h): 
        for j in range(w): 
            key = getNodeKeyFromCode(forest[i][j])
            coloredForest[i][j] = getColoredText(STATES[key]["color"]["r"], 
                    STATES[key]["color"]["g"], STATES[key]["color"]["b"], STATES[key]["symbol"])

    # Print the initial state of the grid graphically colored
    print("\n")
    printGrid(t, coloredForest, w, h)

    # Simulate the fire propagation, while there are nodes on fire
    while(checkElement(forest, nodePos, FIRE)):
        # Calculate the next state for t + 1
        t += 1
        nextState = [[NORMAL for x in range(w)] for y in range(h)]
        
        for i in range(h):
            for j in range(w):
                # State of the current grid node in the forest
                node = forest[i][j]                                
                # If the node is burning, it can't burn anymore
                if(node == FIRE or node == BURNED): nextState [i][j] = BURNED
                # If the nearest neighbor is burning, the fire can propagete to the current node
                elif(node == NORMAL and checkElement(forest, NN(i, j, w, h), FIRE)):
                    # Check the probability to burn
                    if(random.uniform(0, 1) < pThreshold): nextState[i][j] = FIRE

                # Color the forest with the next state update
                key = getNodeKeyFromCode(nextState[i][j])
                coloredForest[i][j] = getColoredText(STATES[key]["color"]["r"], 
                    STATES[key]["color"]["g"], STATES[key]["color"]["b"], STATES[key]["symbol"])
    
        # Set the next state of the forest
        forest = nextState[:]
        # Print the grid graphically colored
        printGrid(t, coloredForest, w, h); 
    
    # Print the number of nodes burned and the amount of steps iterated
    print('Number of nodes burned: ',countElement(forest, nodePos, BURNED),'\n')
    print('Number of iterations: ',t,'\n')