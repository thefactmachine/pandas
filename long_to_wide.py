#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:32:01 2017

@author: markhatcher
"""

import pandas as pd
import numpy as np

# ==== PIVOTING DATA FRAMES =============================================

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

# change the column order...
df_trials = df_trials.loc[: , ['id', 'treatment', 'gender', 'response'] ]
df_trials

df_trials.pivot(index = "treatment", columns = "gender", values = "response")

# ===========================================================================
# ===========================================================================
# ===========================================================================

# long to wide -- version 2

raw_data = {'patient': [1, 1, 1, 2, 2],
        'obs': [1, 2, 3, 1, 2],
        'treatment': [0, 1, 0, 1, 0],
        'score': [6252, 24243, 2345, 2342, 23525]}
 
df = pd.DataFrame(raw_data, columns = ['patient', 'obs', 'treatment', 'score'])
 
df
 
df.pivot(index = 'patient', columns = 'obs', values = 'score')


# ===========================================================================
# ===========================================================================
# ===========================================================================

# long to wide -- version 3 ===


# 12 values -- 7 unique values....
account = [10, 10, 10, 11, 12, 12, 13, 14, 14, 16, 17, 17]
# 12 values -- 8 unique values
alert_code  =  ['a', 'b', 'c', 'd', 'e', 'a', 'f', 'c', 'g', 'h', 'd', 'b']

dict_data = {}
dict_data['id'] = account
dict_data['alert_code'] = alert_code
         
df_data = pd.DataFrame.from_dict(dict_data)

# change the column order...
df_data = df_data[['id', 'alert_code']]

# create a series of booleans...that equals the number of rows.
df_data['bool'] = np.ones((df_data.shape[0],1), dtype=bool)

# now go from long to wide.....
df_data = df_data.pivot(index = 'id', columns = 'alert_code', values = 'bool')

# now set values when 
df_data = df_data.applymap(lambda v: True if v == True else False)

# now sum up the booleans
df_data['total'] = df_data.sum(axis = 1)




