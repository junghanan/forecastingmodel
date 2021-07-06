# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df=pd.read_csv("2021 Summer Data.csv")
print(df.head())
print(df)
print(df.dtypes)

df.rename(columns={'2,021':'2021POS$'}, inplace=True)
df['2021POS$']=np.log(df['2021POS$'])

X=df.Days
X=sm.add_constant(X)
y=df['2021POS$']
mod = sm.OLS(y,X)
res=mod.fit()
print(res.summary())








