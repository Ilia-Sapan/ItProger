import math
import os
import random
import re
import sys


sticks = [1 , 2 , 3 , 4 , 5 , 10]

def maximumPerimeterTriangle(sticks):
    sticks.sort()
    for i in range(len(sticks) - 3, -1, -1):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            return [sticks[i], sticks[i+1], sticks[i+2]]
    return [-1]

print(maximumPerimeterTriangle(sticks))