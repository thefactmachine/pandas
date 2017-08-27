#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:55:55 2017

@author: markhatcher
"""

#  https://chrisalbon.com/python/pandas_indexing_selecting.html
# Create an example dataframe about a fictional army
raw_data = {

            'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', \
                         'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', \
                         'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', \
                        '2nd','1st', '1st', '2nd', '2nd'],
            
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, \
                     1099, 1523],
            
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', \
                       'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', \
                       'Louisana', 'Georgia']
            }
            

import pandas as pd
import numpy as np
 
lst_columns = ['regiment', 'company', 'deaths', 'battles', 'size', \
               'veterans', 'readiness', 'armored', 'deserters', 'origin']

df = pd.DataFrame(raw_data, columns = lst_columns)
 
df

# set the index....
df = df.set_index('origin')



# drop some columns.... axis = 1 means that we are referring to a column not a row

lst_numeric_columns = df.columns.values[[0, 1, 6, 7, 8]]
df = df.drop(lst_numeric_columns, axis = 1)

df.floordiv(12)

# use a numpy function
np.floor_divide(df, 3)

def mult_3(x):
    return x * 3

# using apply is row columsn
df.apply(mult_3)

# using apply map -- applymap is element wise
df.applymap(mult_3)

def fn_range(z):
    return max(z) - min(z)

# apply map will not work in this situation....
df.apply(fn_range)


# apply map applies the function to each element
format = lambda x: '%.2f' % x
df.applymap(format)
 












