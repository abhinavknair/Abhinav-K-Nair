import numpy as np
import math
import matplotlib.pyplot as plt

L=2*10**-8 #length scale in metre
N=100 #no of intervals
x=np.linspace(-L,L,N+1)
d=x[2]-x[1]
h=1.054*10**-34 #reduced planck's constant
m=9.1*10**-31 #mass of e in kg
e=1.6*10**-19 #electronic charge
om=10**13 #harmonic oscillator frequency 

v=(m*(om**2)*x**2)/2 #harmonic oscillator potential 
a=1/(d**2)
H=np.zeros((N-1,N-1))
for i in range(N-1):
   for j in range(N-1):
      if i==j:
         H[i,j]=((h**2/m)*a)+v[i]
      elif np.abs(i-j)==1:
         H[i,j]=((-h**2)/(2*m))*a

eigenvalues, eigenvectors=np.linalg.eigh(H)

energies=eigenvalues/e
energies.sort()

for i in range(0,4):
  E=(i+0.5)*h*om
  y=[]
  y=np.append(y,eigenvectors[:,i])
  y=np.insert(y,0,0) #first value is zero
  y=np.append(y,0) #final value is zero
  print("energy of n=",i,"level is:",energies[i],"eV and theoretical value of E=",E/e,"eV")
  plt.plot(x,y,label='n=%i state'%(i))
plt.title("Harmonic Oscillator")
plt.legend()
plt.grid()
plt.xlabel('x')
plt.ylabel('wave function')
plt.show()
