#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 06:10:01 2022

@author: mkc
"""
# %%   Numpy basics
#   importing

import numpy as np

array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1*15 vector


print(array.shape)

a= array.reshape(3,5)

print("shape: ",a.shape)

print("dimension: ",a.ndim)

print("data type: ", a.dtype.name)

print("size: ",a.size)

print("type: ",type(a))

array1=np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])



zeros=np.zeros((3,4))  #allocation

zeros[0,0]=5
print(zeros)


np.ones((3,4))

np.empty((2,3))


a=np.arange(10,50,5)
print(a)


a=np.linspace(10,50,20)
print(a)

# %%   Numpy Basic Operations


a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))

a<2

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])

# element wise production

print(a*b)

# matrix product

b=b.T # transport
print(a)
print(b)
a.dot(b)

print(np.exp(a))

a=np.random.random((5,5))

print(a.sum())
print(a.max())
print(a.min())

print(a.sum(axis=0))
print(a.sum(axis=1))

print(np.sqrt(a))
print(np.square(a)) #  a**2

print(np.add(a,a))


# %%   Indexing and Slicing


import numpy as np

array=np.array([1,2,3,4,5,6,7]) # vector dimension=1

print(array[0])
print(array[0:4])

reverse_array=array[::-1]
print(reverse_array)


array1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1.ndim)

print(array1[1,1])

print(array1[:,1])

print(array1[1,:])

print(array1[1,1:4])

print(array1[-1,:])

print(array1[:,-1])

# %%   Shape Manipulation


array=np.array([[1,2,3],[4,5,6],[7,8,9]])


#  flatting

a=array.ravel()

array1=a.reshape(3,3)
 
array2=array1.T

print(array2.shape)


array5=np.array([[1,2],[3,4],[4,5]])

# %%   Stacking Arrays


array1=np.array([[1,2],[3,4]])

array2=np.array([[-1,-2],[-3,-4]])

array1([[1, 2],
       [3, 4]])

array2([[-1, -2],
       [-3, -4]])

# vertical

array([[1, 2],
       [3, 4]])
array([[-1, -2],
       [-3, -4]])

array3=np.vstack((array1,array2))

# horizontal 

array([[1, 2],[-1, -2]
       [3, 4]],[-3, -4])

array4=np.hstack((array1,array2))


# %%   Convert  and Copy Arrays


liste=[1,2,3,4]

array=np.array(liste)

liste2=list(array)

a=np.array([1,2,3])

b=a
c=a

b[0]=5

d= np.array([1,2,3])

e=d.copy()

f=d.copy()
