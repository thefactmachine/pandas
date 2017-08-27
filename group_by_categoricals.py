#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:07:17 2017

@author: markhatcher
"""


# == Group By and Catgoricals
# ==========================================================================
import pandas as pd

df_sales = pd.DataFrame({
                    'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
                    'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
                    'bread': [139, 237, 326, 456],
                    'butter': [20, 45, 70, 98]
                }
            )


# filter by column value
df_sales.loc[df_sales['weekday'] == 'Sun']

# returns counts of all four colums
df_sales.loc[df_sales['weekday'] == 'Sun'].count()

# weekday is an index and the three columns 
df_sales.groupby('weekday').count()

# agregating / reducing functions:  mean(), std(), sum(), first(), last()
# min(), max()

# get the sum of bread for each weekday...
df_sales.groupby('weekday')['bread'].sum()


# easy to add multiple columns
df_sales.groupby('weekday')[['bread','butter']].sum()


# group_by multiple columns -- seems to add hierarchical indexes.....
df_sales.groupby(['city','weekday'])['bread'].mean()


# create a series and then add it 
customers = pd.Series(['Dave','Alice','Bob','Alice'])

df_sales['customers'] = customers
        
        
# Categorical Data
# uses less memory and speeds up group_by
df_sales['weekday'] = df_sales['weekday'].astype('category')



# multiple aggregations....
df_sales.groupby('city')[['bread','butter']].agg(['max','sum'])




# custom aggregation ==========================================
def data_range(x):
    return x.max() - x.min()
 
df_sales.groupby('weekday')[['bread', 'butter']].agg(data_range)


# aggregation dictionaries ==========================================
dict_agg = {'bread': 'sum', 'butter':data_range}

df_sales.groupby('customers').agg(dict_agg)

def fn_z_score(z):
    return (z  - z.mean()) / z.std()

df_sales.groupby('city')['butter'].transform(fn_z_score)


def fn_z_year_name(group):
    df = pd.DataFrame(
            {'butter': fn_z_score(group['butter']),
             'city': group['city']})
    return df

df_sales.groupby('city').apply(fn_z_year_name)


# === understanding the groupby object.......................

splitting = df_sales.groupby('weekday')

# prints out dictionary object.
splitting.groups

# returns dictionary
type(splitting.groups)

# print out one group
splitting.groups['Sun']

# print out the first element for the group
splitting.groups['Sun'][0]

print splitting.__class__

print(splitting.groups.keys())

# you just have to accept that splitting is a fairly complex object
for group_name, group in splitting:
    print group_name

for group_name, group in splitting:
    print group


for group_name, group in splitting:
    ave = group['butter'].mean()
    print group_name, ave
    
    
bln_city = df_sales['city'].str.contains('Aust')
    
df_sales.groupby(bln_city)['bread'].sum()

    
    


















