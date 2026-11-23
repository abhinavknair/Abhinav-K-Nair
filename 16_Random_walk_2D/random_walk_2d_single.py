import numpy as np
import matplotlib.pyplot as plt
fig, axes=plt.subplots(2,1,figsize=(6,6))

N=100
n=0 #horizontal position
m=0 #vertical position
x=np.zeros((N))
y=np.zeros((N))
R=np.zeros((N))

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
  x[i]=n
  y[i]=m
  R[i]=n**2+m**2 #squared displacement

axes[0].plot(x,y)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

steps=np.arange(1,N+1,1)
axes[1].plot(steps,R)
axes[1].set_xlabel('steps')
axes[1].set_ylabel('R')
plt.tight_layout()
plt.show()
