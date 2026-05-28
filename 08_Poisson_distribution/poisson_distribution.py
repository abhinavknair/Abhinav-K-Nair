import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x0=np.random.poisson(lam=5,size=(10000,20))
x1=np.random.poisson(lam=5,size=(10000,100))
x2=np.random.poisson(lam=5,size=(10000,1000))

#calculate the arithmetic mean of each vector (row)
means0=np.mean(x0,axis=1) #axis=1 for means of rows & axis=0 for means of columns
means1=np.mean(x1,axis=1)
means2=np.mean(x2,axis=1)
means=[means0,means1,means2]

sns.kdeplot(means,fill=True)
#to plot as histogram & density curve instead, use:
#sns.displot(means,kde=True)
plt.xlabel("means")
plt.ylabel("frequency")
plt.title("Distribution of means of random numbers using Poisson distribution")
plt.show()
