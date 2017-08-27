#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 14:31:57 2017

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

# another way of creating an index.....
# shows how to extract the index of the previous data_frame....
df_a = pd.DataFrame(raw_data, columns = lst_columns, index = df.index.values)


# select a column -- this outputs an array
df['size']
 
# select a few columns
df[['size', 'deaths', 'regiment']]


# select a few columns and a few rows...
df[['size', 'deaths', 'regiment']][0:4]

# select a few columns and a few rows...
df[['size', 'deaths', 'regiment']
 

# get by column number --- implicitly
df[[df.columns.values[x] for x in [2, 1, 5]]]

# WHAT IS THE DIFFERENCE BETWEEN LOC AND ILOC
# loc works on labels....
# iloc works on the positions


# LOC [Row / column]
# SELECTING ROWS -- shows how to use the index...
# get all columns for rows between Arizona and Maine
df.loc['Arizona' : 'Maine']

# select two rows  
df.loc[['Arizona', 'Texas']]

# get a selection of columns for rows between Arizona and Maine
df.loc['Arizona' : 'Maine'][['deaths', 'size']]

# select ALL rows and a specific set of columns
df.loc[:, ['deaths', 'size']]




# ILOC [Row / Column]
# using iloc --- 
# get rows 4 to 7 -- all columns
df.iloc[3:7]
 
# get rows 4 to 7 -- some rows...
df.iloc[3:7, 1:4]


# SELECTION BY CONDITIONALS.
# selecting rows that evaluate to booleans....
df[df['deaths'] > 50]


# deaths are greater than 500 or less than 50
df[(df['deaths'] > 500) | (df['deaths'] < 50)]



# Conditionals with a subset of columns....
df[df['deaths'] > 100][['size', 'deaths', 'regiment']]


# select all the regiments not named "Dragoons"
df[~(df['regiment'] == 'Dragoons')]

# another way of doing things....
df[(df.battles < 5) & (df.size < 1000)]

# =============================================================================
# =============================================================================


            
            

