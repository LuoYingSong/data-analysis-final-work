#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import json
import os
import numpy as np
from tqdm import tqdm


# In[2]:

path='preprocess_data_trans'
file_list = os.listdir(path+'/')


# In[3]:


def test(x):
    data = x['2019-09-30']
    if str(data) == 'nan':
        for detail in x:
            if str(detail) != 'nan':
                return detail
    else:
        return data


total_list = []
code_list = []
for code in tqdm(file_list):
    code_list.append(code)
    df_list = []
    for file_name in os.listdir(path+'/{}'.format(code)):
        df_list.append(pd.read_csv(path+'/{}/{}'.format(code,file_name)))
    df = pd.concat(df_list,axis=0)
    df = df.replace('--',np.nan)
    df = df.replace('</tr>',np.nan)
    df_names = df['报告日期']
    del df['报告日期']
    df.astype('float32')
    try:
        df['2019-09-30'] = df.apply(test,axis=1)
    except KeyError:
        code_list.pop()
        continue
    df_new = df['2019-09-30'].values.T
    total_list.append(df_new)


# In[4]:





# In[5]:




# In[7]:


df = pd.DataFrame(total_list,columns=df_names)
df['code'] = code_list


# In[8]:


df


# In[9]:


df.to_csv('trans1.csv')


# In[ ]:




