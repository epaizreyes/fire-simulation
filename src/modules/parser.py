# -- coding: utf-8 --
"""
Parser of a file containing corresponding parameters.

@author: Evelyn Paiz
"""

# ----------------------------------------------------------
# Imports
import ast                                                  # Processing of trees
import json                                                 # Json files
from modules.color import getColoredText                    # Color for the printed text
# ----------------------------------------------------------

def evaluateParams(data):
    # Evaluate the dimension of the grid (integer and > 0)
    if(not(isinstance(data["widthGrid"], int)) or data["widthGrid"] < 0): return False
    if(not(isinstance(data["heightGrid"], int)) or data["heightGrid"] < 0): return False

    # Evaluate the burning probability (integer or float but 1 <= p >= 0)
    if(isinstance(data["burningProbability"], int)): data["burningProbability"] = float(data["burningProbability"])
    if(not(isinstance(data["burningProbability"], float)) or 
        data["burningProbability"] < 0 or data["burningProbability"] > 1): return False

    # Evaluate the initial fire positions
    if(not(isinstance(data["initFire"], list))): return False
    else:
        # Check each one of the input positions
        for x in range(len(data["initFire"])):
            pos = data["initFire"][x]
            if(not(isinstance(pos, list)) or len(pos) != 2): return False
            elif(pos[0] >= data["heightGrid"] or pos[1] >= data["widthGrid"]): return False

    # Al tests passed
    return True

def parseJSON(file):
    """
    parse function returns the set of parameters parsed
    from a input file.

    :param file: file to be parsed
    :return: list of parameters
    """
     # Open the file
    with open(file) as f:
        data = json.load(f)

    if(evaluateParams(data)): return data
    else:
        print(getColoredText(255, 0, 0, 'Input parameters not properly defined, please check'))
        exit()

def parseText(file):
    """
    parse function returns the set of parameters parsed
    from a input file.

    :param file: file to be parsed
    :return: list of parameters
    """
    # Parameters to be returned
    params={}

    # Open the file
    with open(file) as f:

        # Read lines
        for line in f:
            try:
                if(line[0:9] == "widthGrid"):
                    params["widthGrid"] = int(line[10:-1])
                    
                if(line[0:10] == "heightGrid"):
                    params["heightGrid"] = int(line[11:-1])
                    
                if(line[0:18] == "burningProbability"):
                    params["burningProbability"] = float(line[19:-1])
                    
                if(line[0:8] == "initFire"):
                    params["initFire"] = ast.literal_eval(line[9:-1])
            except Exception as e:
                print(getColoredText(255, 0, 0, 'Input parameters not properly defined, please check'))
                exit()

    return params