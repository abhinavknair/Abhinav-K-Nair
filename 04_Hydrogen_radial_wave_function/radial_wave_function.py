import numpy as np
import math
import matplotlib.pyplot as plt
r_min=7*10**-2
r_max=20 # in angstrom
N=300 #no of intervals
r=np.linspace(r_min,r_max,N+1)
d=r[2]-r[1]

h1=1973 #h1=hbar*c (unit=eVAngstrom)
m=0.511*10**6 #eV/c^2
e=3.795 #(eVAngstrom)^1/2
l=int(input("value of l:"))

v=(-e**2/r)+((h1**2)*l*(l+1))/(2*m*r**2) #radial wave effective potential 

H=np.zeros((N-1,N-1))
for i in range(N-1):
   for j in range(N-1):
      if i==j:
         H[i,j]=(h1**2)/(m*d**2)+v[i]
      elif np.abs(i-j)==1:
         H[i,j]=(-h1**2)/(2*m*d**2)
eigenvalues, eigenvectors=np.linalg.eigh(H)
energies=eigenvalues
energies.sort()

for i in range(0,2):
  R=[]
  R=np.append(R,eigenvectors[:,i]/r[i])
  R=np.insert(R,0,0) #first value is zero
  R=np.append(R,0) #final value is zero
  print('energy of n=%i level is:%2.4feV'%(i,energies[i]),"& Theoretical value:",-13.6/(i+l+1)**2,"eV")
  plt.plot(r,abs(R),label='n=%i state'%(i))
plt.legend()
plt.grid()
plt.title("Radial wave for H-atom")
plt.xlabel('r')
plt.ylabel('wave function (R)')
plt.show()
