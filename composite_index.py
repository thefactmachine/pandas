#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:59:44 2017

@author: markhatcher
"""
import pandas as pd


# create the data.......................
lst_vol = [14070500, 21701800, 19189500, 29736800,
           20085900, 18460400, 16726400, 11808600, 21453100]
 
lst_ticker = ['CSCO', 'AAPL', 'MSFT', 'AAPL', 'MSFT', 'CSCO',
              'MSFT', 'CSCO', 'AAPL']
 
lst_prices = [31.50, 112.52, 57.42, 113.00, 57.24,
            31.35, 57.64, 31.59, 113.05]
 
lst_dates = ['2016-10-03', '2016-10-03', '2016-10-03', '2016-10-04',
             '2016-10-04', '2016-10-04',
             '2016-10-05', '2016-10-05', '2016-10-05']
 
dict_data = {}
dict_data['date'] = lst_dates
dict_data['price'] = lst_prices
dict_data['volume'] = lst_vol
dict_data['ticker'] = lst_ticker
 
df_stock_data = pd.DataFrame.from_dict(dict_data)
df_stock_data


# convert the string to date
df_stock_data['date'] = pd.Series([pd.to_datetime(date)
                            for date in df_stock_data['date']])


# ===========SET A COMPOSITE INDEX ==================================

df_stock_data = df_stock_data.set_index(['ticker', 'date'])


print(df_stock_data.index)

# sort the index...
df_stock_data.sort_index()

df_stock_data = df_stock_data.sort_index()

# get both columns
df_stock_data.loc[('AAPL', pd.to_datetime('2016-10-03'))]

# get the volume column only....
df_stock_data.loc[('AAPL', pd.to_datetime('2016-10-03')), 'volume']


# Slicing -- outermost index ....V1
df_stock_data.loc['AAPL']

# Slicing -- outermost index ....V2
df_stock_data.loc['AAPL': 'CSCO']


# fancy indexing -- outermost  index
df_stock_data.loc[(['AAPL', 'CSCO'], pd.to_datetime('2016-10-03')), :]


df_stock_data.loc[(slice(None), slice('2016-10-03', '2016-10-04')),:]






