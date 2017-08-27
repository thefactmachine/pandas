#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:07:40 2017

@author: markhatcher
"""


#  https://chrisalbon.com/python/pandas_indexing_selecting.html
# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', \
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
                       'Louisana', 'Georgia']}

import pandas as pd
 
lst_columns = ['regiment', 'company', 'deaths', 'battles', 'size', \
               'veterans', 'readiness', 'armored', 'deserters', 'origin']

df = pd.DataFrame(raw_data, columns = lst_columns)
 
df

# set the index....
df = df.set_index('origin')

# the following provides an array of booleans for each columns.  Where the 
# column is tested for whether it contains any zeros...  In the following...the
# only column which has any zeros if armoured...
# so the all() predicate means those columns whose values are ALL NON ZERO
df.all()

# so the following will not print out armoured.....
df.loc[:, df.all()]

# Any = Return whether any element is True over requested axis

# prints true for all columns
df.any()

df['size'] = 0

# now prints False for size only....  
df.any()

# drops the size column...
df.loc[:, df.any()]

# prints only the size column....
df.loc[:, ~(df.any())]

# ============================================================================
# =============================================================================
# ==  Create a New Data Frame.....

df = pd.DataFrame(raw_data, columns = lst_columns)
 
df

# Nulls are NaN......

import numpy as np

# set the 'armoured' and 'deaths' columns to nan if battles is greater than 20
df.loc[df.battles > 20, ['armored', 'deaths']] = np.nan

# show columns where values are nan
df.loc[:, df.isnull().any()]


# get the column names - same as above but extracts
df.loc[:, df.isnull().any()].columns.values

# complement of the above
df.loc[:, df.notnull().all()].columns.values

# drops the rows which have any nana
# 11 rows here not 12...
df.dropna(how = 'any')
       
df.dropna(how = 'any').shape
         
df.shape








       
       
       







