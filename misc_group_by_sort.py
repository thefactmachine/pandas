#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:57:19 2017

@author: markhatcher
"""



import pandas as pd
test_data = [
                {'id': 2, 'group': 'B',  'text': 'mary had'},
                {'id': 5, 'group': 'A',  'text': 'black mat.'},
                {'id': 3, 'group': 'A',  'text': 'sat on the'},
                {'id': 6, 'group': 'B',  'text': 'lamb.'},
                {'id': 1, 'group': 'A',  'text': 'The cat'},
                {'id': 4, 'group': 'B',  'text': 'a little'}
            ]
 
df_test = pd.DataFrame(test_data)  


# lets be explicit about the column order.....
lst_col_order = ['id', 'group', 'text']
df_test = df_test[lst_col_order]
 

# now we sort by row order.....
df_test = df_test.sort_values(by = ['id', 'group'], ascending = [True, True])

splitting = df_test.groupby('group')

# this gets the index values.
splitting.groups['A'].values
                
                
 
import pandas as pd
from io import StringIO
 
data = StringIO(u"""
"name1","hej","2014-11-01"
"name1","du","2014-11-02"
"name1","aj","2014-12-01"
"name1","oj","2014-12-02"
"name2","fin","2014-11-01"
"name2","katt","2014-11-02"
"name2","mycket","2014-12-01"
"name2","lite","2014-12-01"
""")
 
df = pd.read_csv(data,header=0, names=["name","text","date"],parse_dates=[2])


# add column with month

# add column with month
df["month"] = df["date"].apply(lambda x: x.month)

# concatenate the text of all rows....
df_new = df.groupby(['name'])['text'].apply(lambda x: ' '.join(x)).reset_index()
            

test_string = """the quick brown fox jumped over the dog"""
 
lst_test_string = test_string.split(" ")
 
lst_test_string.count("the")
 
# returns the first occurance.
lst_test_string.index("the")



                





