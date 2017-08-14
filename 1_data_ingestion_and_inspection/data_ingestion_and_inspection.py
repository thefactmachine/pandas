# -*- coding: utf-8 -*-
"""
pandas 101 
"""


import pandas as pd

aapl = pd.read_csv('/Users/markhatcher/TEMP_not_on_cloud/pandas_101/data_sets/aapl.csv', 
                   index_col = 'Date', 
                   parse_dates = True)

# ipython use "clear" to clear the screen

type(aapl)

# get the dimensions
aapl.shape

# get the columns
aapl.columns

# get the data type of columns
type(aapl.columns)

# print the type of index.
aapl.index

# get the first 5 rows and all columns
aapl.iloc[:5,:]

# as above but with columns 3,4,5
aapl.iloc[:5,2:5]

# get the 5 rows at the end
aapl.iloc[-5:,:]

# get the first two rows
aapl.head()

# get the final 10 rows
aapl.tail(10)

# gets summary information
aapl.info()

# see how things are zero indexed
aapl.iloc[0:10, :]

aapl.head(2)

import numpy as np

# this gets the first 10 rows and the last column
aapl.iloc[0:10, -1]

# this assigns every third column as nan
aapl.iloc[::3, -1] = np.nan
aapl.head(9)

low = aapl['Low']

# this prints out a series. This belongs to pandas
type(low)

# this will be a type of numpy array
lows = low.values
type(lows)

# ============================================================================
# BUILDING A DATA FRAME FROM SCRATCH
# ============================================================================

tips = pd.read_csv('/Users/markhatcher/TEMP_not_on_cloud/pandas_101/data_sets/tips.csv', 
                   index_col = 0)


print(tips)

tips.shape[1]

# ============================================================================
# DATA FRAME FROM DICTIONARY
# ============================================================================
data =      {
            'weekday': ['Sun', 'Sun', 'Mon', 'Mon'], 
            'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
            'visitors': [139, 237, 326, 456],
            'signups': [7, 12, 3, 5]
            }

data['city'][0:2]

users = pd.DataFrame(data)

print(users)


# ============================================================================
# DATA FRAME FROM DICTIONARY  II
# ============================================================================

cities = ['Austin', 'Dallas', 'Austin', 'Dallas']

signups = [7, 12, 3, 5]

visitors = [139, 237, 326, 456]

weekdays = ['Sun', 'Sun', 'Mon', 'Mon']

list_labels = ['city', 'signups', 'visitors', 'weekday']

list_cols = [cities, signups, visitors, weekdays]


zipped = list(zip(list_labels, list_cols)) 

print(zipped)

data = dict(zipped)

new_users = pd.DataFrame(data)

# ============================================================================
# Broadcasting ==  goes to an entire column
# ============================================================================

new_users['new_col'] = 0

print(new_users)

# ============================================================================

# ============================================================================
# Broadcasting - with a dictionary
# ============================================================================

heights = [ 59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1 ]

data_dict = {'gender': 'male', 'height': heights}

results = pd.DataFrame(data_dict)

print(results)

# ============================================================================
# Using index and columns
# ============================================================================

results.columns = ['sex', 'height in']
print(results)

results.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

print(results)



# ============================================================================
# Reading in a csv file
# ============================================================================

filepath = '/Users/markhatcher/TEMP_not_on_cloud/pandas_101/data_sets/ISSN_D_tot.csv'
sunspots = pd.read_csv(filepath)

sunspots.iloc[10:20, :]

sunspots.info()
# ===== using header = none

sunspots = pd.read_csv(filepath, header = None)
sunspots.iloc[10:20, :]

# ===== using names keyword

col_names = ['year', 'month', 'day', 'dec_date',  'sunspots', 'definite']

sunspots = pd.read_csv(filepath, header = None, names = col_names)

sunspots.iloc[10:20, :]

# iloc is integer location



# ============================================================================
# Using NA
# ============================================================================



# = using NA values version I

sunspots = pd.read_csv(filepath, header = None, 
                       names = col_names,
                       na_values = '-1')
sunspots.iloc[10:20, :]

# = using NA values version II
sunspots = pd.read_csv(filepath, header = None, 
                       names = col_names,
                       na_values = ' -1')
sunspots.iloc[10:20, :]

# = using NA values version III
sunspots = pd.read_csv(filepath, header = None, 
                       names = col_names,
                       na_values = {'sunspots':[' -1']})

sunspots.iloc[10:20, :]


# ============================================================================
# Using parse_dates
# ============================================================================

sunspots = pd.read_csv(filepath, header = None, 
                       names = col_names,
                       na_values = {'sunspots':[' -1']}, 
                       parse_dates = [[0, 1, 2]]
                       )

sunspots.iloc[10:20, :]

sunspots.info()

# ============================================================================
# defining an index
# ============================================================================

# define which columns will be the index
sunspots.index = sunspots['year_month_day']
sunspots.info()

sunspots.index.name = 'date'
sunspots.info()


# ============================================================================
#  Including only relevant columns
# ============================================================================

cols = ['sunspots', 'definite']
sunspots = sunspots[cols]
sunspots.iloc[10:20, :]

# ============================================================================
#  Writing to csv and xsls
# ============================================================================

# out_csv = 'sunspots.csv'
# sunspots.to_csv(out_csv)
# out_tsv = 'sunspots.tsv'
# sunspots.to_csv(out_tsv, sep='\t')
# out_xlsx = 'sunspots.xlsx'
# sunspots.to_excel(out_xlsx)         


# ============================================================================
#  Plotting Stuff - Not Done
# ============================================================================

