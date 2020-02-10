#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:00:08 2020

@author: flpbraun
"""

import pandas as pd
import simplejson as json
import requests

path = '/home/flpbraun/PS_Linx/part_02/'
file = 'input-dump.json'
save_path = '/home/flpbraun/PS_Linx/part_02/'

with open(path + file) as f:
    df_dump = pd.DataFrame(json.loads(line) for line in f)
    
df_dump = df_dump.sort_values(by = ['productId'])
df_dump = df_dump.reset_index(drop=True)

for url in list(df_dump['image']):
    response = requests.get(url)
    if response.status_code == 200:
        pass
    else:
        df_dump = df_dump[df_dump.image != url]
        
df_dump = df_dump.reset_index(drop=True)

df_dump1 = pd.DataFrame(columns = ['productId','image'])

for i in list(range(0,len(df_dump))):
    df_aux = df_dump.iloc[i]
    prod_id = df_aux['productId']
    serie_aux = df_dump1.pivot_table(index=['productId'], aggfunc='size')
    if len(serie_aux) == 0:
        df_dump1 = df_dump1.append(df_aux)
    elif df_dump1['productId'].iloc[-1] != prod_id:
        df_dump1 = df_dump1.append(df_aux)
    elif serie_aux[prod_id] < 3:
        df_dump1 = df_dump1.append(df_aux)
    else:
        pass
    
df_dump1.to_csv(save_path + 'sanitize_dump.csv', index=False)
