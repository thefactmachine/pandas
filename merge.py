#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 18:08:21 2017

@author: markhatcher
"""


import pandas as pd
from IPython.display import display
from IPython.display import Image
 

 
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_a
 
raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_b
 
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data, columns = ['subject_id','test_id'])
df_n
 
df_a.shape[0] == df_b.shape[0]
 
# ===========================================================================
# ===========================================================================
# ===========================================================================


# join data frames VERTICALLY.....rbind
df_new = pd.concat([df_a, df_b])
df_new
 

# join data frames HORIZONTALLY.....rbind
df_new_horiz = pd.concat([df_a, df_b], axis=1)
df_new_horiz
 
 
pd.merge(df_new, df_n, on='subject_id')


# merge with a LEFT join
pd.merge(df_a, df_b, on='subject_id', how='left')



