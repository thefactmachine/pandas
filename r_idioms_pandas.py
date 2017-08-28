#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:57:37 2017

@author: markhatcher
"""


import pandas as pd
import numpy as np

# ==== Comparison to R idioms -------------------------------------
# http://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html
# long to wide --- version 1
 
id = [1, 2, 3, 4]
tm = ['A', 'A', 'B', 'B']
gen = ['F', 'M', 'F', 'M']
res = [5, 3, 8, 9]
 
dict_trials = {}
dict_trials['id'] = id
dict_trials['treatment'] = tm
dict_trials['gender'] = gen
dict_trials['response'] = res
 
df_trials = pd.DataFrame.from_dict(dict_trials)



# get the first 2 rows....
df_trials.iloc[:2]

# FILTER query based on two different columns.......
df_trials[(df_trials.gender == 'F') &  (df_trials.id == 1) ]

# DELETE columns
df_trials.drop(['id', 'treatment'], axis = 1)

# DISTINCT 
df_trials[['gender']].drop_duplicates()

df_trials[['gender', 'treatment']].drop_duplicates()

# SAMPLE
df_trials.sample(2)

# COLUMN RENAME
df_trials.rename(columns = {'gender' : 'sex', 'id': 'pk'})

# MUTATE
df_trials.assign(new_col = df_trials.response - df_trials.id)

# SUMMARY STATISTICS
df_trials.describe()

#GROUP_BY
df_trials.groupby('gender').agg({'response': 'mean', 'id': 'sum'})

dict_group = {'response': 'sum', 'id': 'mean'}

df_trials.groupby('gender').agg(dict_group)

# SELECT NON CONTINTUOUS COLUMNS / ROWS
# combined the following with pandas commands.....
np.r_[:3, 24:30]


df_trials.iloc[: ,1:3]

# %IN%
s = pd.Series(np.arange(5),dtype=np.float32)
s.isin([0, 2, 7])

# select rows by boolean
df_trials[df_trials['id'] < 3]

lst_treatment = ['A', 'C', 'D']

df_trials[df_trials['treatment'].isin(lst_treatment)]









df_trials.iloc[1:3 ,1:3]

