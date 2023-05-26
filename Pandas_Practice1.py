import numpy as np
import pandas as pd

from numpy.random import randn
#Series
#Dataframes
#Missing Data
# Groupby
#Merging, joining and  concatenating
# operations
# data input and  output

labels = ['a','b','c'] #list
my_data = [10,20,30]  #list
arr = np.array(my_data) #array
d={'a':10,'b':20} #dictionary

print(pd.Series(data=arr))
print(pd.Series(labels,my_data))
#cls
#print(randn(5,4))
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

print(df['W']['A'])

#print(pd)