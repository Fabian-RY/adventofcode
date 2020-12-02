# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:41:21 2020

@author: fabia
"""
import re


valids = 0

with open('Day2.txt') as fhand:
    for line in fhand:
        expression = re.match('(\d+)-(\d+)\s+([a-z]):\s+([a-z]+)', line)
        values = expression.groups()
        times = values[3].count(values[2])
        min_ = values[0]
        max_ = values[1]
        if (times >= int(values[0]) and times <= int(values[1])):
            valids += 1
#print(valids)

valids = 0

with open('Day2.txt') as fhand:
    for line in fhand:
        expression = re.match('(\d+)-(\d+)\s+([a-z]):\s+([a-z]+)', line)
        values = expression.groups()
        password = values[3]
        pos1 = int(values[0])-1
        pos2 = int(values[1])-1
        letter = values[2]
        print(letter, pos1, password[pos1], pos2, password[pos2])
        valids += (password[pos1] == letter) ^ (password[pos2] == letter)
        print(valids)