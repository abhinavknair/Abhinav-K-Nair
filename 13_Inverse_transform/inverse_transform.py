import numpy as np
import math

lam=2
U=np.random.uniform(0,1,1)
print('U=',U)

P=np.zeros((15))
for i in range (0,15):
  P[i]=(np.exp(-lam)*lam**i)/math.factorial(i)
  P[i]=P[i-1]+P[i] #the cumulated Poisson probability (say, F(k)) as an array
print('F(k)=',P)

#the corresponding Poisson-distributed random number is given by the upper k value of the interval in F(k) within which the value of the uniform random number sits
for i in range(0,15):
  if P[i-1]<=U<=P[i]:
    X=i
if U<P[0]:
  X=0
print("X=",X)

#x - unifomly distributed random no
#X - Poisson distributed random no
