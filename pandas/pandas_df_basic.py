import pandas as pd
import numpy as np

df1= pd.DataFrame(data=[1,2,3,4,5], index=['a','b','c','d','e'], columns=['number']);
print (df1)
print (df1.sum())

print (df1.ix['a'])

df2=df1.apply(lambda  x:x**2)
df2.columns=['another_number']
#new column by caclate existing columns
df1['num2'] = df1['number'] **2
#new column by new list
df1['num3'] = [6,7,8,9,10]
print (df1)

#join 2 dataframe using index
print (df1.join(df2, how='inner'))

#create date time index
dates = pd.date_range(start='2018-01-01', periods=10, freq='20B')
print (dates)

np1=np.random.standard_normal((10,4))
print (np1)
np1=np1.round(6)

df3=pd.DataFrame(data=np1, index=dates)
print (df3)

print (np.array(df3).round(4))

print (df3.sum())
df3.plot()
np.sqrt(df3)

###########Group By######################
df3['Quarter']=['Q1','Q1','Q2','Q2','Q3','Q3','Q3','Q4','Q4','Q4']
print (df3)

grp1=df3.groupby('Quarter')
grp1.mean()