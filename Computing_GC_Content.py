# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:12:57 2021

@author: VISHAKMADHWARAJKADAM
"""

import os

os.chdir('E:/Downloads')

# Opening theRosalind File
DNA = open('rosalind_gc.txt', 'r')
DNA = DNA.readlines()
DNA_dict = {}
for lines in DNA:
    if '>Rosalind' in lines:
        key = lines
        DNA_dict[key] = ''
    else:
        lines = lines.replace('\n', '')
        DNA_dict[key] = DNA_dict[key] + lines
        
# Finding GC% content
for keys in DNA_dict.keys():
    G = DNA_dict[keys].count('G')
    C = DNA_dict[keys].count('C')
    DNA_dict[keys] = ((G + C) / len(DNA_dict[keys])*100)

DNA_max = max(DNA_dict, key = DNA_dict.get)