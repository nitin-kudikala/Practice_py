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
print(df)

df['totalwx'] = df['W'] + df['X']
print(df)

#print(pd)

#remove the column
df.drop('totalwx',axis=1) #this will be return and df without the column, but would actually remove the column
#axis - 0 for rows, 1 for column
df.drop('totalwx',axis=1,inplace=True) #this will actually drop the column from main df

#droping the row we would need axis as 0 which is default
df.drop('E')

df.loc[['A','E'],['W','Y']]


#conditioni
df[df['W']>0]

df[df['W']>0]['X']


#for multple condition we & or | as operator  instead of  normal python and ,or
df[(df['W']>0) & (df['X']>1)]

#reset index, to reset to numerical
df.reset_index()

newind = 'MH GJ KA TS DL'.split()

df['states'] = newind

# this will set the states as index, this will basically override old index
df.set_index('states')


