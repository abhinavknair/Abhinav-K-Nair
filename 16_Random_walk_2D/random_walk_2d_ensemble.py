import numpy as np
import matplotlib.pyplot as plt

walks=1000
N=100
x=np.zeros((walks,N))
y=np.zeros((walks,N))
R=np.zeros((walks,N))

for j in range(walks):
  n=0 #horizontal position
  m=0 #vertical position
  for i in range(N):
    choice=np.random.choice(4)
    if choice==0:
      n+=1
    elif choice==1:
      n-=1
    elif choice==2:
      m+=1
    elif choice==3:
      m-=1
    x[j,i]=n
    y[j,i]=m
    R[j,i]=n**2+m**2

msd=np.zeros((N))
for j in range(N):
  for i in range(1,walks):
    R[i,j]=R[i-1,j]+R[i,j]
  msd[j]=R[i,j]/walks
print('msd=',msd)

steps=np.arange(1,N+1,1)
plt.plot(steps,msd,color='green')
plt.xlabel('steps')
plt.ylabel('msd')
plt.grid()
plt.show()
