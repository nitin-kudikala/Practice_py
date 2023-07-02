#matrix plots
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

tc = tips.corr() # correlation of tips data set
#print(tc)
#sns.heatmap(tc,annot=True)
print(flights)
fp = flights.pivot_table(index='month',columns='year',values='passengers')
print(flights.pivot_table(index='month',columns='year',values='passengers'))
#sns.heatmap(fp,cmap='coolwarm')

#sns.clustermap(fp,cmap='coolwarm',standard_scale=1)

sns.PairGrid() #pairgrid gives allow customize for pairplot





plt.show()