# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:01:38 2017

@author: Adwait
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    longestlist=[]
    sum1=0
    for n in range(len(L)):
        list1=[]        
        list1.append(L[n])
        for k in range(n+1,len(L)):
            if L[k]>=L[k-1]:
                list1.append(L[k])
            else:
                break
        if len(list1)>len(longestlist):
            longestlist=list(list1)
    
        list2=[]        
        list2.append(L[n])
        for k in range(n+1,len(L)):
            if L[k]<=L[k-1]:
                list2.append(L[k])
            else:
                break
        if len(list2)>len(longestlist):
            longestlist=list(list2)
    for p in longestlist:
        sum1+=p
    return sum1