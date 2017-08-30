#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 19:07:37 2017

@author: markhatcher
"""

import numpy as np

data1 = [6, 7.5, 8, 0, 1]

# use the array constructor
arr1 = np.array(data1)

# get the data type
arr1.dtype

# vectorised operations.
arr1 * 3

arr1 + arr1

# 2d array
data2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# get the number of dimensions...
 data2.ndim

# declare 3 x 6 array of zeros
np.zeros((6,3))

np.ones(13)

# creating with different data types.....

arr1 = np.array([1, 2, 3], dtype=np.float64)


arr2 = np.array([1, 2, 3], dtype=np.int32)
 
 
arr3 = np.array([1, 1, 0], dtype=np.bool)

# CASTING
arr = np.array([1, 2, 3, 4, 5])
arr.dtype

float_arr = arr.astype(np.float64)

float_arr.dtype

# ARRAY SLICES  ARE VIEWS ON THE ORIGINAL ARRAY.....
# THIS MEANS THAT THE DATA IS NOT COPIED....

arr = np.arange(10)

arr_slice = arr[5:8]

# LOOK --- we think we are taking a copy but....
arr_slice[1] = 1234567

arr

arr_slice[:] = 64
         
arr

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

arr3d[1]

arr3d[1][0]

arr3d[1][0][2]

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# BOOLEAN INDEXING.........

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7, 4)

# results in a boolean array 
names == 'Will'


data = np.random.randn(7,3)

# positions 2, 4 true
data[names == 'Will']


data[names == 'Will', 2:]

# Boolean with NEGATION......

data[names != 'Will', 1:]


# Combining Boolean Expressions
mask = (names == 'Bob') | (names == 'Will')
data[mask]

# Boolean operatons on elements...
data[data < 7] = 0
    
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# FANCY INDEXING.........
arr = np.empty((8, 4))

for i in range(8):
    arr[i] = i
 
arr[3]

arr[[3, 2, 0, 6]]

# negative indexes...selects rows from the end......
arr[-3]


arr = np.arange(32).reshape((8, 4))

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

# TRANSPOSING ARRAYS......

arr = np.arange(15).reshape((3, 5))

# 3 x 5
arr

# 5 x 3
arr.T

# The following computes the matrix product.....
np.dot(arr.T, arr)


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

# UNIVERSAL FUNCTIONS......

# Universal functions...ufunc is a function that performs elementwise operations
# on data in ndarrays....

arr = np.arange(10)
 
arr

np.sqrt(arr)


# we also have binary functions.......

# start, stop, step
x = np.arange(100, 110, 1)

y = np.arange(50, 60, 1)

np.maximum(x, y)

np.add(x, y)

# SEE PAGE 112.....




# Conditional Logic As Array Operations........

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = np.where(cond, xarr, yarr)


# ANY --- ALLL

bools = np.array([False, False, True, False])
bools.any()


bools.all()


# UNIQUE AND OTHER SET LOGIC.....
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

np.unique(names)

# OTHER SET FUNCTIONS.....
# unique(x), intersect1d(x, y), in1d(x, y), setdiff1d(x, y)

values = np.array([6, 0, 0, 3, 2, 5, 6])
 
np.in1d(values, [2, 3, 6])

 
 




# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# Chapter 12 Explains Broadcasting......






















      
       

    
    
    
    
    
    














 










 
 




