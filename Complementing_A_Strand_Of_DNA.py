# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:54:32 2021

@author: VISHAKMADHWARAJKADAM

This python script contains code for getting a complementing strand of a given DNA Strand
"""
import os

os.chdir('E:/Downloads')

# Opening the Rosalind File
DNA = open('rosalind_revc (1).txt', 'r')
DNA = DNA.read()

# Finding the Reverse Complement of a string
new_DNA = ''
for i in range(-1, -len(DNA) -1, -1):
    if DNA[i] == 'A':
        new_DNA = new_DNA + 'T'
    if DNA[i] == 'T':
        new_DNA = new_DNA + 'A'
    if DNA[i] == 'G':
        new_DNA = new_DNA + 'C'
    if DNA[i] == 'C':
        new_DNA = new_DNA + 'G'