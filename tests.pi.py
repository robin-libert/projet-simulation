# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:05:24 2018

@author: Robin Libert
"""
import piAnalyse as pa
import piRandom as r
import math

"""
The parameter is the list of the number of occurrences of each events.
Return Kn of khi2
"""
def khi2(listReal):
    sizeEch = 0
    for e in listReal:
        sizeEch += e
    print(sizeEch)
    r = 10
    p = 1/10
    Kn = 0
    for i in range(r):
        Kn += ((listReal[i] - (sizeEch*p)) / math.sqrt(sizeEch * p))**2
        return Kn
    
if(__name__ == "__main__"):
    listReal = pa.countOccurences(r.randomIntList(1000000))
    print(khi2(listReal))