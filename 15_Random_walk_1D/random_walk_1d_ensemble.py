import random
import math
import matplotlib.pyplot as plt

walks=10 #number of independent walks
N=20 #total steps
p=0.5
q=1-p
n1=np.zeros((walks))
P_n=np.zeros((walks))
X=np.zeros((walks))
X_sq=np.zeros((walks))
for j in range(walks):
  n=0
  for i in range(N):
    prob_left=random.random() #generates a random probability
    if prob_left<p:
      n+=1
    else:
      n+=0
  n1[j]=n
  X1=2*n-N #displacement
  X[j]=X1
  X_sq[j]=X1**2 #squared displacement
  P=(math.factorial(N)/(math.factorial(n)*math.factorial(N-n)))*(p**n)*(q**(N-n))
  P_n[j]=P
print('X=',X)
X2=X.copy() #making a copy of X for future use

#mean
for j in range(1,walks):
  X[j]=X[j-1]+X[j]
#print(X)
mean_X=X[j]/walks
print('mean_X=',mean_X)

#variance
Y=(X2-mean_X)**2
print('Y=',Y)
for j in range(1,walks):
  Y[j]=Y[j-1]+Y[j]
var_X=Y[j]/walks
print('var_X=',var_X)

#mean-square displacement
print('X_sq=',X_sq)
for j in range(1,walks):
  X_sq[j]=X_sq[j-1]+X_sq[j]
mean_X_sq=X_sq[j]/walks
print('mean_X_sq=',mean_X_sq)

#print('n1=',n1)
#print('P_n=',P_n)

plt.bar(n1,P_n)
plt.xlabel('n')
plt.ylabel('P_n')
plt.show()
