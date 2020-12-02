# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:45:50 2020

@author: fabia
"""

expenses = list()
with open("Day1-1.txt") as fhand:
    for line in fhand:
        expenses.append(int(line.strip('\n')))


def get_sum_equal_2020(expenses):
    for i in range(len(expenses)):
        for j in range(i+1, len(expenses)):
            if expenses[i] + expenses[j] == 2020:
                return (expenses[i], expenses[j])
    else:
        return None
    
i, j = get_sum_equal_2020(expenses)
print(i+j, i*j)

def get_three_sum_equal_2020(expenses):
    for i in range(len(expenses)):
        for j in range(i+1, len(expenses)):
            for k in range(j+1, len(expenses)):
                if expenses[i]+expenses[j]+expenses[k] == 2020:
                    return (expenses[i],expenses[j],expenses[k])
                    
    else:
        return None
    
i, j, k = get_three_sum_equal_2020(expenses)
print(i,j,k, i*j*k)