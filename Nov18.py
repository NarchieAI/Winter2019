# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Final Exercise - in Sypder (in directory tracked by git)
# Create a function that converts the argument into a string
# Create a function that takes two lists as arguments, 
    # checks whether the two lists have overlapping elements
    # and either returns the duplicated elements or provides a nice message
# Create a function that tries to replace index 0 of the argument passed 
    # with the word "pancakes"
    # don't bother with exception handling for the moment
# Create a new python file and save it in the same directory
# Import the functions from the previous file into the new file
# In the new file, check what the functions do using the help function (you better have added docstrings)
# Test the functions you've created, determine when they break and when they don't
# Extra credit: re-implement the pancakes function so that it works when a list, string or tuple is passed
# Commit completed code to your GitHub account
    

def conv_str(a):
    ''' convert argument to string'''
    return str(a)

def dup_check(a,b):
    ''' check if the two lists have overlapping elements
    return overlapping elements in a list, or an empty list if none'''
    dup = []
    for el in a:
        if el in b:
            dup.append(el)
    return dup

def replace0(wrd,hd):
    ''' repleace first element with what's given'''
    lst = list(wrd)
    print(lst)
    lst[0] = hd
    wrd1 = ''
    for el in lst:
        wrd1 += el
    return wrd1

