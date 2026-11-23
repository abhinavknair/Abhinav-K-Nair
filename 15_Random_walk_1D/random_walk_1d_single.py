import numpy as np
import random
import math
import matplotlib.pyplot as plt

N=100 #total steps
p=0.5 #probability of going to the right
X=np.zeros((N))
R=np.zeros((N))
n=0 #position of the walker
for i in range(N):
  prob_left=random.random() #generates a random probability
  if prob_left<p:
    n+=1
  else:
    n-=1
  X[i]=n
  R[i]=n**2 #squared position
print('X=',X)

#counting
bins_n=np.arange(-N,N+1,1) #intervals for counting
counts_n=np.zeros(len(bins_n)-1,dtype=int) #array to store counts
for j in X:
  for i in range(len(bins_n)-1):
    low=bins_n[i]
    high=bins_n[i+1]
    if low<=j<high:
      counts_n[i]+=1
      break
print('counts_n=',counts_n)
X2=X.copy()

#mean
for j in range(1,N):
  X[j]=X[j-1]+X[j]
mean_X=X[j]/N
print('mean X',mean_X)

#variance
Y=(X2-mean_X)**2
for j in range(1,N):
  Y[j]=Y[j-1]+Y[j]
var_X=Y[j]/N
print('var X=',var_X)

#mean-squared displacement (msd)
for j in range(1,N):
  R[j]=R[j-1]+R[j]
msd=R[j]/N 
print('msd=',msd)

prob_n=counts_n/N
plt.plot(bins_n[:-1],prob_n)
plt.xlabel('position (X)')
plt.ylabel('prob')
plt.title('Single Random Walk')
plt.show()
