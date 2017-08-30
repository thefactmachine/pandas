#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:27:39 2017

@author: markhatcher
"""

# A series....

import pandas as pd
import numpy as np

obj = pd.Series([4, 7, -5, 3])

# get the values is an "Array"
obj.values

# get the index
obj.index.values

# create a Series with an explicit Index
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])


# COMPARED WITH A NUMPY ARRAY ... you can use values in the index when 
# selecting single values or a set of values.....

obj2['b']

obj2[['b', 'c']]

# This returns false because we are looking at the index....

# this returns false
7 in obj2

# this returns true
'a' in obj2

# this returns true
7 in obj2.values

# CREATION FROM DICTIONARY....
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

obj3 = pd.Series(sdata)
obj3



# set a value to NULL
obj3['Oregon']  = np.NAN

# test for nulls ELEMENT WISE
pd.isnull(obj3) 

pd.notnull(obj3)
   
   
# with INDEXING you can automatically ALIGN a series....
states = ['California', 'Ohio', 'Oregon', 'Texas']
# create a slightly different object...
obj4 = pd.Series(sdata, index=states)

obj3 + obj4


obj4[0] = 4000

print(obj4)

# A series has a name attribute...dunno why...maybe for columns.
obj4.name = 'population'

obj4.index.name = 'state'

print(obj4)

# An index can be completly replaced...
obj4.index = ['NSW', 'ACT', 'VIC', 'WA']

print(obj4)


# but a SINGLE element CANNOT be replaced
obj4.index[2] = 'QLD'


# A DATA FRAME HAS BOTH A ROW AND A COLUMN INDEX.....
# WHILE A DATA FRAME IS 2D....More dimensions can be represented by 
# hierarchical indexes....

# CONSTRUCTING A DATA FRAME.................

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

# we specify the columns in a specific order....
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])

# page 116

# RETRIEVING A COLUMN ------nate that the index is the same as the data frame
# 1) dict like notation....
frame['state']

# 2) -- attribute notation 
frame.state

# retrieve rows by index....
frame.ix[2:3]


# CONSTRUCTING A DATA FRAME.............# nested dictionaries...
 pop = {'Nevada': {2001: 2.4, 2002: 2.9}, \
'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop)

# TRANSPOSIING.....
frame3.T

# can returns the values in an array type object
frame3.values

# but what happens if we add a column of text...
frame3['nice'] = ['non', 'oui', 'non']

# converts alles to strings...
frame3.values

# INDEX OBJECTS.....

# There is a whole stack of index methods and properties....

# HERE
# append diff intersection union isin delete drop insert is_monotonic is_unique unique

# REINDEXING --- can fill values...

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
 
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value = 0)

# Here is how to reindex the columns....

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], \
                   columns=['Ohio', 'Texas', 'California'])

states = ['Texas', 'Utah', 'California']

frame.reindex(columns=states)

states = ['Texas', 'Utah', 'California']
# WE DO REINDEXING MUCH MORE EASILY WITH IX......
frame.ix[['a', 'b', 'c', 'd'], states]


# DROPPING ROWS..

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], \
                   columns=['Ohio', 'Texas', 'California'])

# drop from rows....
frame.drop(['a', 'c'])

# drop from columns...
frame.drop(['Ohio', 'Texas'], axis = 1)


# INDEXING, SELECTION AND FILTERING......

# https://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation/




























   
          
          




