import numpy as np
import math

lam=2
x=np.random.uniform(0,1,1)
print('x=',x)
P=np.zeros((1,15))

for i in range (0,15):
  P[0,i]=(np.exp(-lam)*lam**i)/math.factorial(i)
  P[0,i]=P[0,i-1]+P[0,i] #the cumulated Poisson probability (say, F(k)) as an array
print('F(k)=',P)

#the corresponding Poisson-distributed random number is given by the upper k value of the interval in F(k) within which the value of the uniform random number sits
for i in range(0,15):
  if P[0,i-1]<=x<=P[0,i]:
    X=i
    print("X=",i)
if x<P[0,0]:
  X=0
  print("X=",0)

#x - unifomly distributed random no
#X - Poisson distributed random no
