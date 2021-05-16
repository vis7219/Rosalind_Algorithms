# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:49:38 2021

@author: VISHAKMADHWARAJKADAM
"""


import os
os.chdir('E:/Downloads')

# Opening theRosalind File
DNA = open('rosalind_rna.txt', 'r')
DNA = DNA.read()

# Replacing T with U
DNA = DNA.replace('T', 'U')
print(DNA)