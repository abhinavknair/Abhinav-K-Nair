import numpy as np
import math
import matplotlib.pyplot as plt
r_min=0.03
r_max=5 #in angstrom
N=300 #no of intervals
r=np.linspace(r_min,r_max,N+1)
d=r[2]-r[1]

a=[1,3,10] #screening parameter 

h1=1973 #h1=hbar*c (unit=eVAngstrom)
m=0.511*10**6 #eV/c^2
e=3.795 #(eVAngstrom)^1/2
l=0

H=np.zeros((N-1,N-1))
for k in range(len(a)):
   for i in range(N-1):
      for j in range(N-1):
         if i==j:
            v[i]=(-e**2/r[i])*np.exp(-r[i]/a[k])+((h1**2)*l*(l+1))/(2*m*r[i]**2)
            H[i,j]=(h1**2)/(m*d**2)+v[i]
         elif np.abs(i-j)==1:
            H[i,j]=(-h1**2)/(2*m*d**2)

   eigenvalues, eigenvectors=np.linalg.eigh(H)
   energies=eigenvalues
   energies.sort()

   R=[]
   R=np.append(R,eigenvectors[:,0]/r[i]) #ground-state wavefuncion for every value of 'a'
   R=np.insert(R,0,0) #first value is zero
   R=np.append(R,0) #final value is zero
   plt.plot(r,abs(R),label='a=%i state'%(a[k]))
   print('energy of a=',a[k],'state is:',energies[0],'eV')
plt.legend()
plt.grid()
plt.title("Screened Coulomb potential")
plt.xlabel('r (angstrom)')
plt.ylabel('wave function (R)')
plt.show()
