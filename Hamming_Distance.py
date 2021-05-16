# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:28:20 2021

@author: VISHAKMADHWARAJKADAM
"""

import os

os.chdir('E:/Downloads')

# Opening theRosalind File
DNA = open('rosalind_hamm.txt', 'r')
DNA = DNA.read().split('\n')

# Finding Hamming Distance
count = 0
for i in range(len(DNA[0])):
    if DNA[0][i] != DNA[1][i]:
        count = count + 1
