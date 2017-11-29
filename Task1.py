# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:58:19 2017

@author: sanga
"""

def getCommonElements(L1, L2):
    print("Elements common to both L1 and L2")
    l = len(L1)
    m = len(L2)
    i,j = 0,0
    while i<l and j<m:
        if L1[i] < L2[j]:
            i += 1
        elif L2[j] < L1[i]:
            j += 1
        else:
            print(L1[i])
            j += 1
            i += 1

            
def getElementsInList1(L1, L2):
    print("Elements present in L1 and not L2")
    print([i for i in L1 if not i in L2 or L2.remove(i)])
                    
            
L1 = ['a' , 'b', 'c']
L2 = ['b', 'd']
getCommonElements(L1, L2)
getElementsInList1(L1, L2)

#L1 = ['a', 'b' , 'c', 'd', 'e']
#L2 = ['b', 'e']

#L1 = ['a', 'c', 'd', 'e']
#L2 = ['b', 'f']