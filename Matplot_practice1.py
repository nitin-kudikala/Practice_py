import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0,5,11) # spread/divide the numbers from 0 to 5 to give you 11 numbers
y = x**2

#plt.plot(x,y)
plt.xlabel('X lable') # label x axis
plt.ylabel('Y lable') # label y axis
plt.title('XY title') # set title of thechart
# plt.show()

#create multiple plot on same screen using subplot

plt.subplot(1,2,1) # row,column,index(position of sub graph)
plt.plot(x,y,'r') #r red

plt.subplot(1,2,2)
plt.plot(y,x,'b') #b is for blue color of line on graph
plt.show()

#Figure object is use to have more  control over the plot graph

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8]) #left,bottom,width,height

axes.plot(x,y)

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)

#plt.tight_layout()
plt.show()

axes[0].set_xlabel('x lable')
axes[0].set_ylabel('y lable')

plt.show()

#muliple plots

fig,axes = plt.subplots(nrows=2,ncols=2) #2 by 2 view with 4 charts
fig.savefig('my_picturefig.jpg')
plt.show()

#axes.plot(x,y)