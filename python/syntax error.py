#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:29:26 2022

@author: mkc
"""

# %%   syntax error

print(9)
 # print 9
# int 10.0 


# %%   exceptions

a=10
b="2"
liste=[1,2,3]
print(sum(liste))

print(a+b)
print(str(a)+b)
k=10
print(k)

# %%   Except



try:
    1/0
except:
        print("except")
else:
        print("else")
finally:
        print("done")



try:
    1/1
except:
    print("except")
else:
    print("else")
finally:
    print("done")
