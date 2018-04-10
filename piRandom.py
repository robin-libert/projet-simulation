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
def seed():
    index = int((my_age()*1000000) % 999999)
    return index

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
    index = seed()
    decalage = 0
    randomNumber = []
    for e in range(n):
        if(e % 1000 == 0):
            old = index
            index = (seed()*(old+1))%999999
            print(index)
        randomNumber.append(pi_decimals[(index+decalage)%999999])
        decalage += 42
    return randomNumber
    
if(__name__ == "__main__"):
    plt.title('Nombre d\'occurences de 0...9 dans\n le premier million de décimales de PI\n Zoom sur les valeurs critique')
    plt.xlabel("Valeur du nombre que l'on compte")
    plt.ylabel("Nombre d'occurences")
    x = [0,1,2,3,4,5,6,7,8,9]
    y = pa.countOccurences(randomIntList(1000000))
    plt.axis([-1,10,99000,101000])
    plt.bar(x,y)
    plt.tight_layout()
    #plt.savefig("data/hist_pi_digits_occurences_zoom.png", pad_inches=0)
    plt.show()