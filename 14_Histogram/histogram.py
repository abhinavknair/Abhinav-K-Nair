import numpy as np
import matplotlib.pyplot as plt

x=np.random.uniform(0,1,100)

bins=np.arange(0,1,0.1) #bins edges: [0.0, 0.1, ..., 0.9]
#there are len(bins)-1=9 actual bins: [0.0,0.1), [0.1,0.2), ..., [0.8,0.9)
counts=np.zeros(len(bins)-1,dtype=int)
for j in x:
  for i in range(len(bins)-1):
    low=bins[i]
    high=bins[i+1]
    if low<=j<high:
      counts[i]+=1
      break
print(counts)

#x-coordinates for bars should be the left edges of the bins (bins[:-1])
plt.bar(bins[:-1],counts,width=bins[1]-bins[0],align='edge',edgecolor='black')
plt.xlabel("range")
plt.ylabel("counts")
plt.title("uniform random numbers (x)")
plt.grid()
plt.show()
