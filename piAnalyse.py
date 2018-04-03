# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:22:27 2018

@author: Robin Libert
"""

import matplotlib.pyplot as plt
import random

pi_file = open("1millionpi.txt", "r")
pi = ""
for line in pi_file:
   pi += line.rstrip('\n\r.')
pi_decimals = list(pi[1:])#list of each decimal of pi
for n in range(len(pi_decimals)):
    pi_decimals[n] = int(pi_decimals[n])


"""
This function count how many of each number between 0 and 9 within the first
million of PI's decimals. Return a list of int.
list[0] = number of 0
list[1] = number of 1
etc
"""
def countOccurences(l):
    n_occurences = [0,0,0,0,0,0,0,0,0,0]
    for n in range(len(l)):
        n_occurences[l[n]] += 1
    return n_occurences

def getPiDecimals(start, end):
    new_pi_decimals =[]
    for e in range(start, end):
        new_pi_decimals.append(pi_decimals[e])
    return new_pi_decimals

def python_random_list(size):
    r = []
    for i in range(size):
        r.append(random.randint(0, 9))
    return r

if(__name__ == "__main__"):
    x = [0,1,2,3,4,5,6,7,8,9]
    y = countOccurences(pi_decimals)
    plt.axis([-1,10,99000,101000])
    plt.bar(x,y)
    plt.show()
    
    x = [0,1,2,3,4,5,6,7,8,9]
    y = countOccurences(python_random_list(1000000))
    plt.axis([-1,10,99000,101000])
    plt.bar(x,y)
    plt.show()