# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:57:21 2018

@author: Robin Libert
"""

import time
import datetime
import math

pi_file = open("1millionpi.txt", "r")
pi = ""
for line in pi_file:
   pi += line.rstrip('\n\r.')
pi_decimals = list(pi[1:])#list of each decimal of pi
for n in range(len(pi_decimals)):
    pi_decimals[n] = int(pi_decimals[n])

"""
This function return my age in seconds.
"""
def my_age():
    my_birth = datetime.date(1994, 4, 14)
    timestamp = time.mktime(my_birth.timetuple())  # time in second between EPOCH and my birth
    #time in second since I was born
    return time.time()-timestamp #time since EPOCH - time between EPOCH and my birth

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
This function return a pseudo random number based on the middle square method.
"""
def middleSquare(n):
    if(n<=3):#car n > 4 pour que cette fonction fonctionne
        n+=4
    new = n*n
    s = str(new)
    l = len(s)
    indexBegin = int(math.ceil(l/4))
    indexEnd = int(math.ceil(l*(2/3))+1)
    s1 = s[indexBegin:indexEnd]
    answer = int(s1)
    return answer


"""
Return a list of size n wich contains random int between 0 and 9
"""
def randomIntList(n):
    index = seed()
    decalage = 0
    randomNumber = []
    ms = middleSquare(index)
    for e in range(n):
        if(e % 100000 == 0):
            index = seed()
            decalage = 0
            ms = middleSquare(index)
        randomNumber.append(pi_decimals[(index+decalage)%999999])
        decalage += (ms%100)+1#plus un si ms vaut 0
    return randomNumber
    
if(__name__ == "__main__"):
#    plt.title('Nombre d\'occurences de 0...9 dans\n 1 million de décimales généré par notre générateur')
#    plt.xlabel("Valeur du nombre que l'on compte")
#    plt.ylabel("Nombre d'occurences")
#    x = [0,1,2,3,4,5,6,7,8,9]
#    y = pa.countOccurences(randomIntList(1000000))
#    plt.axis([-1,10,99000,101000])
#    #plt.axis([-1,10,90000,110000])
#    plt.bar(x,y)
#    plt.tight_layout()
#    plt.savefig("data/hist_mygenerator_digits_occurences_zoom2.png", pad_inches=0)
#    plt.show()
    
#    l = []
#    for i in range(1000000):
#        l.append(random.randint(0,9))
#    plt.title('Nombre d\'occurences de 0...9 dans\n 1 million de décimales généré par le générateur de python')
#    plt.xlabel("Valeur du nombre que l'on compte")
#    plt.ylabel("Nombre d'occurences")
#    x = [0,1,2,3,4,5,6,7,8,9]
#    y = pa.countOccurences(l)
#    plt.axis([-1,10,99000,101000])
#    #plt.axis([-1,10,90000,110000])
#    plt.bar(x,y)
#    plt.tight_layout()
#    #plt.savefig("data/hist_pythongenerator_digits_occurences_zoom2.png", pad_inches=0)
#    plt.show()
    print(myRandom())