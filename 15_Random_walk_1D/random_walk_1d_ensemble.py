import random
import math
import matplotlib.pyplot as plt

walks=10 #number of independent walks
N=20 #total steps
p=0.5
q=1-p
n1=np.zeros((1,walks))
P_n=np.zeros((1,walks))
X=np.zeros((1,walks))
X_sq=np.zeros((1,walks))
for j in range(walks):
  n=0
  for i in range(N):
    prob_left=random.random() #generates a random probability
    if prob_left<p:
      n+=1
    else:
      n+=0
  n1[0,j]=n
  X1=2*n-N #displacement
  X[0,j]=X1
  X_sq[0,j]=X1**2 #squared displacement
  P=(math.factorial(N)/(math.factorial(n)*math.factorial(N-n)))*(p**n)*(q**(N-n))
  P_n[0,j]=P
print('X=',X)
X2=X.copy() #making a copy of X for future use

#mean
for j in range(1,walks):
  X[0,j]=X[0,j-1]+X[0,j]
#print(X)
mean_X=X[0,j]/walks
print('mean_X=',mean_X)

#variance
Y=(X2-mean_X)**2
print('Y=',Y)
for j in range(1,walks):
  Y[0,j]=Y[0,j-1]+Y[0,j]
var_X=Y[0,j]/walks
print('var_X=',var_X)

#mean-square displacement
print('X_sq=',X_sq)
for j in range(1,walks):
  X_sq[0,j]=X_sq[0,j-1]+X_sq[0,j]
mean_X_sq=X_sq[0,j]/walks
print('mean_X_sq=',mean_X_sq)

#print('n1=',n1)
#print('P_n=',P_n)

n1=n1.flatten() #flattening to convert 2D matrix into 1D array
P_n=P_n.flatten()
plt.bar(n1,P_n)
plt.xlabel('n')
plt.ylabel('P_n')
plt.show()
