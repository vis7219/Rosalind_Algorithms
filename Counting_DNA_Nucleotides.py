# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:31:04 2021

@author: VISHAKMADHWARAJKADAM
"""

import os

os.chdir('E:/Downloads')

# Opening theRosalind File
DNA = open('rosalind_dna.txt', 'r')
DNA = DNA.read()

# Counting A,C,G & T in the DNA string
nucleotide_count = [DNA.count(nucleotide) for 
                    nucleotide in 
                    ['A', 'C', 'G', 'T']]

print(nucleotide_count)