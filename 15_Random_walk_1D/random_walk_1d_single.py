import numpy as np
import random
import math
import matplotlib.pyplot as plt

N=100 #total steps
p=0.5 #probability of going to the right
x=np.zeros((N))
R=np.zeros((N))
n=0 #position of the walker
for i in range(N):
  prob_left=random.random() #generates a random probability
  if prob_left<p:
    n+=1
  else:
    n-=1
  x[i]=n
  R[i]=n**2 #squared position
print('x=',x)

#counting
bins_x=np.arange(-N,N+1,1) #intervals for counting
counts_x=np.zeros(len(bins_x)-1,dtype=int) #array to store counts
for j in x:
  for i in range(len(bins_x)-1):
    low=bins_x[i]
    high=bins_x[i+1]
    if low<=j<high:
      counts_x[i]+=1
      break
print('counts_x=',counts_x)
x2=x.copy()

#mean
for j in range(1,N):
  x[j]=x[j-1]+x[j]
mean_x=x[j]/N
print('mean x',mean_x)

#variance
Y=(x2-mean_x)**2
for j in range(1,N):
  Y[j]=Y[j-1]+Y[j]
var_x=Y[j]/N
print('var x=',var_x)

#mean-squared displacement (msd)
for j in range(1,N):
  R[j]=R[j-1]+R[j]
msd=R[j]/N 
print('msd=',msd)

prob_x=counts_x/N
plt.plot(bins_x[:-1],prob_x)
plt.xlabel('position (x)')
plt.ylabel('prob')
plt.title('Single Random Walk')
plt.show()
