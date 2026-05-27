import numpy as np
import math
import matplotlib.pyplot as plt

L=1*10**-8 #length of the well in metre
N=100 #no of intervals
x=np.linspace(0,L,N+1)
d=x[2]-x[1]

h=1.054*10**-34 #reduced planck's constant
m=9.1*10**-31 #mass of e in kg
e=1.6*10**-19 #electronic charge 

H=np.zeros((N-1,N-1))
for i in range(N-1):
   for j in range(N-1):
      if i==j:
         H[i,j]=(h**2)/(m*d**2)
      elif np.abs(i-j)==1:
         H[i,j]=-(h**2)/(2*m*d**2)

eigenvalues, eigenvectors=np.linalg.eigh(H)
print("eigenvalues=\n", eigenvalues)
print("eigenvectors=\n", eigenvectors)

energies=eigenvalues/e
energies.sort()

for i in range(0,3):
  y=[]
  y=np.append(y,eigenvectors[:,i])
  y=np.insert(y,0,0) #first value is zero
  y=np.append(y,0) #final value is zero
  print('energy of n=%i level is:%2.4feV'%(i,energies[i]),"& theoretical value=",((i+1)**2*(h**2)*(np.pi**2))/(2*m*e*L**2),"eV")
  plt.plot(x,y,label='n=%i state'%(i))
plt.title("Particle in a box")
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('wave function (ψ)')
plt.show()
