import numpy as np
import random
import math
import matplotlib.pyplot as plt

N=100 #total steps
p=0.5
q=1-p
X=np.zeros((1,N))
X_sq=np.zeros((1,N))
bins_n=np.arange(-N,N+1,1) #intervals for counting
counts_n=np.zeros(len(bins_n),dtype=int) #array to store counts
n=0 #number of steps (not the right steps)
for i in range(N):
  prob_left=random.random() #generates a random probability
  if prob_left<p:
    n+=1
  else:
    n-=1
  X[0,i]=n #position of walker
  X_sq[0,i]=n**2
print('X=',X)

#counting
for j in X.flatten():
  for i in range(len(bins_n)):
    low=bins_n[i]
    high=bins_n[i+1]
    if low<=j<high:
      counts_n[i]+=1
      break
print('counts_n=',counts_n)
X2=X.copy()

#mean
for j in range(1,N):
  X[0,j]=X[0,j-1]+X[0,j]
mean_X=X[0,j]/N
print('mean x=',mean_X)

#variance
Y=(X2-mean_X)**2
for j in range(1,N):
  Y[0,j]=Y[0,j-1]+Y[0,j]
var_X=Y[0,j]/N
print('var X=',var_X)

#mean-square displacement
for j in range(1,N):
  X_sq[0,j]=X_sq[0,j-1]+X_sq[0,j]
mean_X_sq=X_sq[0,j]/N
print('mean X sq=',mean_X_sq)

#prob_n=counts_n/N
print('pron_n=',prob_n)
plt.plot(bins_n,prob_n)
plt.xlabel('position (X)')
plt.ylabel('prob')
plt.show()
