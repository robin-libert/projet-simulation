# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:41:26 2018

@author: USER
"""

import piAnalyse as pa
import time
import datetime

pi_decimals = pa.pi_decimals

"""
return my age in seconds
"""
def my_age():
    my_birth = datetime.date(1994, 4, 14)
    timestamp = time.mktime(my_birth.timetuple())  # time in second between timestamp and my birth
    #time in second since I was born
    return time.time()-timestamp #time since timstamp - time between timestamp and my birth
    
if(__name__ == "__main__"):
    print(pi_decimals)