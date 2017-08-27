#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:48:26 2017

@author: markhatcher
"""

import pandas as pd
import numpy as np

# create a basic series
prices = [10.70, 10.86, 10.74, 10.71, 10.79]
shares = pd.Series(prices)

# add an index to the series.
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
shares = pd.Series(prices, index = days)
print(shares)

# print the index
print(shares.index)

# give the index a name
shares.index.name = 'weekday'

# you can modify ALL the index entries but not just one or two (immutable)
shares.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


# create a data frame from a dictionary.....

# create unemployment data.frame
lst_zip = [1001, 1002, 1003, 1005, 1007]
lst_unemployment  = [0.06, 0.09, 0.17, 0.10, 0.05]
lst_particpants = [13801, 24551, 11477, 4086, 11362]
 
dict_data = {
                'zip' : lst_zip,
                'rate': lst_unemployment,
                'numbers': lst_particpants
             }


df_unemployment = pd.DataFrame.from_dict(dict_data)


# rejig column order
df_unemployment.loc[:, ['zip', 'rate', 'numbers']]


# assign the zip column to be the index
df_unemployment.index = df_unemployment['zip']


# remove the zip column....
del df_unemployment['zip']

