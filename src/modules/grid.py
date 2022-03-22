# -- coding: utf-8 --
"""
Functions to evaluate nodes inside a grid.

@author: Evelyn Paiz
"""

# ----------------------------------------------------------
# Imports
from modules.color import getColoredText                    # Color for the printed text
# ----------------------------------------------------------

def NN(i, j, w, h):
    """
    NN function returns the set of positions from the 
    nearest neighbors of a node in a grid.

    :param i, j: coordinates of the node in the grid
    :param w: width of the grid
    :param h: height of the grid
    :return: list of indices from the nearest neighbors
    """
    index = []
    if(j > 0): index.append([i, j-1])               # Left neighbor
    if(i < h-1): index.append([i+1, j])             # Bottom neighbor
    if(j < w-1): index.append([i, j+1])             # Right neighbor
    if(i > 0): index.append([i-1, j])               # Top neighbor

    return index

def countElement(grid, listindex, element):
    """
    countElement function returns the number of nodes
    represented by certain element or state.

    :param grid: grid where to search on
    :param listindex: list of indices to be checked in the grid 
                      in the form [[i, j], ...]
    :param element: element or state to search for
    :return: number of nodes represented by the element
    """
    count = 0
    for index in listindex:
        # Check that each index is correctly defined as [i, j],
        # if not print the error
        try:
            if(grid[index[0]][index[1]] == element): count += 1
        except Exception as e:
            print(getColoredText(255, 0, 0, 'Indices are not properly defined as [i, j]: '+ e))
    return count

def checkElement(grid, listindex, element): 
    """
    checkElement function returns true if one node is represented 
    by certain element or state.

    :param grid: grid where to search on
    :param listindex: list of indices to be checked in the grid 
                      in the form [[i, j], ...]
    :param element: element or state to search for
    :return: true or false depending if a node is by the element
    """
    for index in listindex:
        # Check that each index is correctly defined as [i, j],
        # if not print the error
        try:
            if(grid[index[0]][index[1]] == element): return True
        except Exception as e:
            print(getColoredText(255, 0, 0, 'Indices are not properly defined as [i, j]: '+ e))
    return False

def printGrid(t, grid, w, h):
    """
    printGrid function prints graphically a grid in the console.

    :param grid: grid to be printed
    """
    # Print the grid
    print("t: ", t, "\n")
    print("\n".join([" ".join(["{}"]*w)]*h).format(*[x for y in grid for x in y]))
    print("\n")