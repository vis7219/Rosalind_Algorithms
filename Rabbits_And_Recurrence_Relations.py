# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:08:05 2021

@author: VISHAKMADHWARAJKADAM
"""


import os
import numpy as np

os.chdir('E:/Downloads')

# Finding the no. of rabbit after N months
pairs = 2
months = 31
rabbit_pairs = [1,1]

# Looping through months and summing the no. of rabbits in (N-1) & (N-2) months
for i in range(2, months + 1):
    rabbits = rabbit_pairs[i-1] + rabbit_pairs[i-2]*pairs
    rabbit_pairs.extend([rabbits])
    

