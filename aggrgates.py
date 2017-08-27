#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 14:00:01 2017

@author: markhatcher
"""

test_numbers = {
            'id': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            'number': [10, 20, 3, 4, 20, 21, 5],
            'string': ['this', 'is' 'a', 'test', 'string', 'and', 'another', 'seven']
        }

import pandas as pd

df_numbers = pd.DataFrame(test_numbers)

# summary functions
df_numbers['number'].mean()
df_numbers['number'].std()
df_numbers['number'].median()
df_numbers['number'].quantile(0.25)
df_numbers['number'].quantile([0.25, 0.5, 0.75])

df_numbers['number'].min()
df_numbers['number'].max()

df_numbers['number'].describe()

# unique values
df_numbers['number'].unique()

# number of unique values
df_numbers['number'].unique().size

df_numbers['string'].str.upper()  

# get a logical vector
df_numbers['string'].str.contains('test')


# sum the logical vector
df_numbers['string'].str.contains('test').sum()

import numpy as np

# ipython -- turn off pretty printing -- so we can see all the dates
%pprint
 
# get a range of dates from Feb to March
arr_date = np.arange('2005-02', '2005-03', dtype='datetime64[D]')
print(arr_date)

