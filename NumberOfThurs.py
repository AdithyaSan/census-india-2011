# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:38:29 2017

@author: sanga
"""
#Importing the necessary packages
from datetime import datetime
from datetime import timedelta as td
from collections import Counter as cnt

#Start and end dates. Since the question mentioned 1990 and 2000, the beginning and end of
#the respective years have been taken.
start_date = datetime(1990, 1, 1)
end_date = datetime(2000, 12, 31)

#Using timedelta to add dates in the considered range of difference in end and start dates
days_diff = [start_date + td(i) for i in range((end_date-start_date).days+1)]

#Using strftime to convert the tuples to a dict
days_dict = dict(cnt(diff.strftime('%a') for diff in days_diff))

#Printing number of Thursdays from the dict
print("Number of Thursdays: " + str(days_dict['Thu'])) 
