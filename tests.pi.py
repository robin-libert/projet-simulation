# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:05:24 2018

@author: Robin Libert
"""
import piAnalyse as pa
import piRandom as r
import math
import random

pi_decimals = pa.pi_decimals

"""
Return the occurrences of gap of size >= index+1 associate to digit n
The limit size of a gap is set to 100.
"""
def gapList(randomNumberList, n):
    gapList = [0]*100
    gap = 1
    begin = False
    for e in randomNumberList:
        if begin == True and e == n:
            if(gap <= 100):
                gapList[gap-1] += 1
            gap = 1
        elif begin == False and e == n:
            begin = True
        elif begin == True and e != n:
            gap += 1
    acc = 0
    for e in range(-1,-len(gapList)-1,-1):
        acc += gapList[e]
        gapList[e] = acc      
    return gapList

def pokerList(randomNumberList):
    pokerList = [0]*5
    c = 0
    nOccurences = [0]*10
    n=0
    for e in randomNumberList:
        if c < 5:
           nOccurences[e] += 1
        if c == 4:
           for i in nOccurences:
               if i != 0:
                   n += 1
           pokerList[n-1] += 1
           n = 0
           c = -1
           nOccurences = [0]*10
        c += 1
    return pokerList
    

"""
The parameter is the list of the number of occurrences of each events.
Return Kn of khi2 and we have to look khi2 with 9 ddl
"""
def khi2(listReal):
    sizeEch = 0
    for e in listReal:
        sizeEch += e
    Kn = 0
    for i in range(10):
        p = sizeEch*1/10
        Kn += ((listReal[i] - p) / math.sqrt(p))**2
    return Kn

"""
return Kn of khi 2 and we have to look khi2 with 49 ddl
""" 
def khi2Gap(listReal):
    sizeEch = 0
    for e in range(50):
        sizeEch += listReal[e]
    Kn = 0
    for i in range(50):
        p = sizeEch*((1/10)*((9/10)**i))
        Kn += ((listReal[i] - p) / math.sqrt(p))**2
    return Kn

"""
return Kn of khi 2 and we have to look khi2 with 4 ddl
""" 
def khi2Poker(listReal):
    sizeEch = 0
    for e in range(5):
        sizeEch += listReal[e]
    Kn = 0
    for i in range(5):
        p = stirling(5,i+1)
        c = 0
        while -(i+1) != c:
            p = p * (10+c)
            c -= 1
        p = p / 10**5
        Kn += ((listReal[i] - (sizeEch*p)) / math.sqrt(sizeEch * p))**2
    return Kn

"""
# Stirling Algorithm
# Cod3d by EXTR3ME
# https://extr3metech.wordpress.com

I see this implementation and after that I had to do the same.
"""
def stirling(n,k):
    n1=n
    k1=k
    if n<=0:
        return 1
     
    elif k<=0:
        return 0
     
    elif (n==0 and k==0):
        return -1
     
    elif n!=0 and n==k:
        return 1
     
    elif n<k:
        return 0
 
    else:
        temp1=stirling(n1-1,k1)
        temp1=k1*temp1
        return (k1*(stirling(n1-1,k1)))+stirling(n1-1,k1-1)
    
if(__name__ == "__main__"):
    r = r.randomIntList(1000000)
    pi = pi_decimals
    python = []
    for i in range(1000000):
        python.append(random.randint(0,9))

    listPoker = pokerList(pi)
    listGap = gapList(pi,9)
    listSimple = pa.countOccurences(pi)
    
    print(khi2(listSimple))
    print(khi2Gap(listGap))
    print(khi2Poker(listPoker))