# -- coding: utf-8 --
"""
Main program for the simulation of the spreading of fire in a forest.

@author: Evelyn Paiz
"""

# ----------------------------------------------------------
# Imports
import sys                                                  # System module
import os.path                                              # Path management
from modules.simulator import simulateFire                  # Simulator of the fire
# ----------------------------------------------------------

file = sys.argv[1]
simulateFire(file)