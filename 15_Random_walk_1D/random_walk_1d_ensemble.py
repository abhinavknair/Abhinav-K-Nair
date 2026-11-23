import random
import numpy as np
import matplotlib.pyplot as plt
fig, axes=plt.subplots(2,1,figsize=(10,10))

walks=1000 #no. of independent random walks
N=100 #total steps
p=0.5 #probability of going to the right
x=np.zeros((walks,N)) #array to store instantaneous position
R=np.zeros((walks,N)) #array to store squared displacement
for j in range(walks):
  n=0
  for i in range(N):
    prob_left=random.random()
    if prob_left<p:
      n+=1
    else:
      n-=1
    x[j,i]=n
    R[j,i]=n**2
print('x=',x)

msd=np.zeros((N))
for i in range(N):
  for j in range(1,walks):
    R[j,i]=R[j-1,i]+R[j,i] #summing over all independent walks for a single position
  msd[i]=R[j,i]/walks

bins_x=np.arange(-N,N+1,1)
counts_x=np.zeros(len(bins_x)-1,dtype=int)
for j in x.flatten():
  for i in range(len(bins_x)-1):
    low=bins_x[i]
    high=bins_x[i+1]
    if low<=j<high:
      counts_x[i]+=1
      break
print('counts_x=',counts_x)

prob_x=counts_x/(N*walks)
axes[0].plot(bins_x[:-1],prob_x)
axes[0].set_xlabel('position')
axes[0].set_ylabel('prob')
axes[0].set_title('Ensemble of random walks')

steps=np.arange(1,N+1,1)
axes[1].plot(steps,msd,color='green')
axes[1].set_xlabel('steps')
axes[1].set_ylabel('msd')
plt.tight_layout()
plt.show()
