# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:05:24 2018

@author: Robin Libert
"""
import piAnalyse as pa
import piRandom as r
import math

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
    
    

"""
The parameter is the list of the number of occurrences of each events.
Return Kn of khi2
"""
def khi2(listReal,p,r):
    sizeEch = 0
    for e in listReal:
        sizeEch += e
    Kn = 0
    for i in range(r):
        Kn += ((listReal[i] - (sizeEch*p)) / math.sqrt(sizeEch * p))**2
    return Kn
    
def khi2Gap(listReal,r):
    sizeEch = 0
    for e in range(r):
        sizeEch += listReal[e]
    Kn = 0
    for i in range(r):
        Kn += ((listReal[i] - (sizeEch*((1/10)*((9/10)**i)))) / math.sqrt(sizeEch * ((1/10)*((9/10)**i))))**2
    return Kn
    
if(__name__ == "__main__"):
    r = r.randomIntList(1000000)
    g = gapList(r,3)

    listReal = pa.countOccurences(r)
    print(khi2(listReal, 1/10,10))
#    print(pa.countOccurences(r))
    print(khi2Gap(g,50))