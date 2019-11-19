# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:15:07 2019

@author: narch
"""

import Nov18 as nv

help(nv.conv_str)
help(nv.dup_check)
help(nv.replace0)

print(nv.conv_str(4324))
try:
    d = dict({})
    print(nv.conv_str(d))
except:
    print('error nv.conv_str')

a = [1,3,'d',5,2]
b = [2,4,2,1,5]
print(nv.dup_check(a,b))
try:
    print(nv.dup_check(4,b))
except:
    print('error nv.dup_check')

print(nv.replace0('pancake','P'))
try:
    print(nv.replace0([2,3],1))
except:
    print('error nv.replace0')
