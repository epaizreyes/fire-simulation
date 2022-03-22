# -- coding: utf-8 --
"""
Color management.

@author: Evelyn Paiz
"""

def getColoredText(r, g, b, text):
    """
    getColoredText function returns a colored text.

    :r, g, b: color to be choosen defined in RGB
    :text: text to be colored
    :return: colored text 
    """
    # Reference: https://stackoverflow.com/questions/56496731/coloring-entries-in-an-matrix-2d-numpy-array
    # Reference: https://www.codegrepper.com/code-examples/python/python+print+error+in+red
    return "\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, text)