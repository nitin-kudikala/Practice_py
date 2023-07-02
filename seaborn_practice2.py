#Categorical plots
import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
#sns.barplot(x='sex',y='total_bill',data=tips)

#sns.countplot(x='sex',data=tips)# y axis wouldbe just count of x
#sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')

#sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)


plt.show()