import random
import numpy as np
import matplotlib.pyplot as plt

walks=1000 #no. of independent random walks
N=100 #total steps
p=0.5
X=np.zeros((walks,N)) #array to store instantaneous position
X2=np.zeros((walks,N))
msd=np.zeros((N)) #array to store mean-square displacement

for j in range(walks):
  n=0
  for i in range(N):
    prob_left=random.random()
    if prob_left<p:
      n+=1
    else:
      n-=1
    X[j,i]=n
    X2[j,i]=n**2
print('X=',X)
print('X flatten=',X.flatten())

for i in range(N):
  for j in range(1,walks):
    X2[j,i]=X2[j-1,i]+X2[j,i] #summing over all independent walks for a single position
  mean_X2=X2[j,i]/walks
  msd[i]=mean_X2

bins_n=np.arange(-N,N+1,1)
counts_n=np.zeros(len(bins_n)-1,dtype=int)
for j in X.flatten():
  for i in range(len(bins_n)-1):
    low=bins_n[i]
    high=bins_n[i+1]
    if low<=j<high:
      counts_n[i]+=1
      break
print('counts_n=',counts_n)

prob_n=counts_n/(N*walks)
plt.figure(figsize=(8,4))
plt.plot(bins_n[:-1],prob_n)
plt.xlabel('position')
plt.ylabel('prob')
plt.title('Ensemble of Random Walks')
plt.show()

step=np.arange(1,N+1,1)
plt.figure(figsize=(8,4))
plt.plot(step,msd,color='green')
plt.xlabel('steps')
plt.ylabel('msd')
plt.show()
