#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:36:10 2019

@author: cannybiscuit
"""

def bubble_sort_algorithm(array):
    
    n = len(array)
    
    # Loop through the entire array
    for i in range(n):

        for j in range(0, n-i-1):
            
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
def main():
    
    array = [25,66,1,4,77,55,13,5,3]
    
    bubble_sort_algorithm(array)
    
    for i in range(len(array)):
        print("%d" %array[i])

main()