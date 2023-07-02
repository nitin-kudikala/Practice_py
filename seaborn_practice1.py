import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # load sample dataset for tips
print(tips.head())

sns.distplot(tips['total_bill'],kde=True) # distribution plot,  bins evel of dist for x 
#kde - kernel density estimation
sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde') # hex show the  scatter dot as hex
sns.pairplot(tips,hue='sex') # pairplot plot all the numerical columns to different charts
plt.show()