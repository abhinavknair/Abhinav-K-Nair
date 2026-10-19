import numpy as np
import matplotlib.pyplot as plt

walks=1000
N=100
R2=np.zeros((walks,N))
msd=np.zeros((N))
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
    #print('n=',n)
    #print('m=',m)
    R2[j,i]=n**2+m**2
    #print('R2=',R2)

for i in range(N):
  for j in range(1,walks):
    R2[j,i]=R2[j-1,i]+R2[j,i]
  mean_R2=R2[j,i]/walks
  msd[i]=mean_R2
print('msd=',msd)

step=np.arange(1,N+1,1)
plt.plot(step,msd,color='green')
plt.xlabel('step')
plt.ylabel('msd')
plt.grid()
plt.show()
