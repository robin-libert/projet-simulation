# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:57:21 2018

@author: USER
"""

import piAnalyse as pa
import matplotlib.pyplot as plt
import time
import datetime
import random

pi_decimals = pa.pi_decimals

"""
This function return my age in seconds.
"""
def my_age():
    my_birth = datetime.date(1994, 4, 14)
    timestamp = time.mktime(my_birth.timetuple())  # time in second between timestamp and my birth
    #time in second since I was born
    return time.time()-timestamp #time since timstamp - time between timestamp and my birth

"""
I take an index with the microseconds since my birth % 999999.
The index give me a decimal of pi.
"""
def index():
    index = int((my_age()*1000000) % 999999)
    return index
    
"""
The seed is a list of 10 indexes generated thanks to index().
"""
def seed():
    s = []
    i = index()
    for e in range(10):
        s.append(i*(e+1)%999999)
    return s

"""
Return a random number [0,1[
"""
def myRandom():
    r = randomIntList(17)#because of float precision
    strvalue = ""
    for e in r:
        strvalue += str(e)
    floatvalue = float(strvalue)
    value = floatvalue / 100000000000000000.
    return value

"""
Return a list of size n wich contains random int between 0 and 9
"""
def randomIntList(n):
    indexes = seed()
    temp = 0
    decalage = 0
    randomNumber = []
    for e in range(n):
        if temp < len(indexes):
            randomNumber.append(pi_decimals[(indexes[temp]+decalage)%999999])
        else:
            temp = 0
            decalage += 1
            randomNumber.append(pi_decimals[(indexes[temp]+decalage)%999999])
        temp += 1
    return randomNumber
    
if(__name__ == "__main__"):
    print(myRandom())
    plt.title('Nombre d\'occurences de 0...9 dans\n le premier million de décimales de PI\n Zoom sur les valeurs critique')
    plt.xlabel("Valeur du nombre que l'on compte")
    plt.ylabel("Nombre d'occurences")
    x = [0,1,2,3,4,5,6,7,8,9]
    y = pa.countOccurences(randomIntList(100000))
    plt.axis([-1,10,9800,10200])
    plt.bar(x,y)
    plt.tight_layout()
    #plt.savefig("data/hist_pi_digits_occurences_zoom.png", pad_inches=0)
    plt.show()