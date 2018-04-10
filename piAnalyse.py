# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:22:27 2018

@author: Robin Libert
"""

import matplotlib.pyplot as plt
import math
import numpy as np

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

"""
This function take as a parameter a list of pi's decimals
and return a list of decimals between index start and end.
"""
def getPiDecimals(l,start, end):
    new_pi_decimals =[]
    for e in range(start, end):
        new_pi_decimals.append(l[e])
    return new_pi_decimals

"""
This function return a list of relatives errors.
Each number between 0 and 9 should appears 100000 times
if pi was a perfect uniform law, because we consider 1 million
digits. As the digits don't follow perfect uniform
law, we return the percentage of error that the occurences
number of each digits are far of 100000.
"""
def rel_error():
    occurences = countOccurences(pi_decimals)
    err = []
    for e in range(len(occurences)):
        err.append(float("%.3f" % math.fabs((occurences[e]/1000)-100)))#limit the floats to 3 decimals
    #np.savetxt("data/err.txt", err, delimiter=' & ', fmt='%.3f', newline=' \\\\\n')
    return err
    
def hist_pi_decimals():
    plt.title('Nombre d\'occurences de 0...9 dans\n le premier million de décimales de PI')
    plt.xlabel("Valeur du nombre que l'on compte")
    plt.ylabel("Nombre d'occurences")
    x = [0,1,2,3,4,5,6,7,8,9]
    y = countOccurences(pi_decimals)
    plt.bar(x,y)
    plt.tight_layout()
    #plt.savefig("data/hist_pi_digits_occurences.png", pad_inches=0)
    plt.show()
    
def hist_pi_decimals_zoom():
    plt.title('Nombre d\'occurences de 0...9 dans\n le premier million de décimales de PI\n Zoom sur les valeurs critique')
    plt.xlabel("Valeur du nombre que l'on compte")
    plt.ylabel("Nombre d'occurences")
    x = [0,1,2,3,4,5,6,7,8,9]
    y = countOccurences(pi_decimals)
    plt.axis([-1,10,99000,101000])
    plt.bar(x,y)
    plt.tight_layout()
    #plt.savefig("data/hist_pi_digits_occurences_zoom.png", pad_inches=0)
    plt.show()
    
if(__name__ == "__main__"):
    test = [[1,2,3],[4,5,6],[7,8,9]]
    np.savetxt("data/test.txt", test, delimiter=' & ', fmt='%.3f', newline=' \\\\\n')
    