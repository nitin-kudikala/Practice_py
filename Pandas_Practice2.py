import numpy as np
import pandas as pd
from numpy.random import randn
#index levels
outside = ['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index =pd.MultiIndex.from_tuples(hier_index)
#multilevel index
df =pd.DataFrame(randn(6,2),hier_index)
print(df)
print(df.loc['G1'].loc[1])

#name the  multi index
df.index.names  = ['Group','Num']

print(df)

#cross section search in multi index
# here we are getting all the Num =1
print(df.xs(1,level='Num'))

# Data missing
#dictionary
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)

print(df)

#here we have  df having missing value mean having NaN, so we can drop the records having the NaN
print(df.dropna())

# if we dont want all the Nan to removed we can put  a  threashold like drop if there more than 2 NaN like below

print(df.dropna(thresh=2))

# we can replace  the Nan using fill

print(df.fillna(value=df['A'].mean()))


#Groupby
data = {'company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'person':['sam','charlie','amy','vanessa','carl','sarah'],
        'sales':[200,120,340,124,243,350]
        }

df = pd.DataFrame(data)
print(df)
#grp = df.groupby('company').sum()
print(df.groupby('company').describe())


#concatination,Merging, joining

#Operation

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,222,444],
                   'col3':['abc','def','ghi','xyz']})
#find unique value
print(df['col2'].unique()) #[444 555 222]
print(df['col2'].nunique()) #3

#find occurance of vallue in column

print(df['col2'].value_counts())

#apply custom function 
def times2(x):
    return x*2

print(df['col2'].apply(times2))

#use lamdba to define inline custom function

print(df['col2'].apply(lambda x: x*2))

#sort
print(df.sort_values('col2',ascending=False))

print(df.isnull())