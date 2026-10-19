import numpy as np
import matplotlib.pyplot as plt

N=100
n=0 #horizontal position
m=0 #vertical position
X=np.zeros((N))
Y=np.zeros((N))
R2=np.zeros((N))

for i in range(N):
  choice=np.random.choice(4) #generates 0, 1, 2, or 3
  if choice==0:
    n+=1
  elif choice==1:
    n-=1
  elif choice==2:
    m+=1
  elif choice==3:
    m-=1
  X[i]=n
  Y[i]=m
  R2[i]=n**2+m**2 #squared displacement
print('X=',X)
print('Y=',Y)
print('R2=',R2)

plt.plot(X,Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
