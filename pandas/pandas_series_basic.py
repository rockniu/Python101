import pandas as pd
import numpy as np

df1= pd.DataFrame(data=[1,2,3,4,5], index=['a','b','c','d','e'], columns=['number']);
print (df1)
s1=df1['number']
print(type(s1))

s2=pd.Series(data=np.arange(2,10,2))
print (s2)