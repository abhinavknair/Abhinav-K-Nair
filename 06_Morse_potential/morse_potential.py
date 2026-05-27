import numpy as np
import math
import matplotlib.pyplot as plt
r_min=0.03
r_max=2 #angstrom
N=300 #no of intervals
r=np.linspace(r_min,r_max,N+1)
d=r[2]-r[1]

h1=1973 #h1=hbar*c (unit=eVAngstrom)
m=470*10**6 #reduced mass of H2 nuclei (eV/c^2)
a=1.44 #width parameter (angstrom)^-1
r0=0.74 #equilibrium bond length (angstrom)
D=4.7 #dissociation energy (eV)
r1=r-r0
v=D*r #defining an arbitrary potential 
H=np.zeros((N-1,N-1))
for i in range(N-1):
   for j in range(N-1):
      if i==j:
         v[i]=D*(np.exp(-2*a*r1[i])-2*np.exp(-a*r1[i]))
         H[i,j]=(h1**2)/(m*d**2)+v[i]
      elif np.abs(i-j)==1:
         H[i,j]=(-h1**2)/(2*m*d**2)
eigenvalues, eigenvectors=np.linalg.eigh(H)
energies=eigenvalues
energies.sort()
R=[]
R=np.append(R,eigenvectors[:,0])
R=np.insert(R,0,0) #first value is zero
R=np.append(R,0) #final value is zero
print('lowest vibrational energy is:',energies[0],'MeV')
plt.plot(r,abs(R),label='ground state')
plt.legend()
plt.grid()
plt.title("Morse potential")
plt.xlabel('length (angstrom)')
plt.ylabel('wave function')
plt.show()
