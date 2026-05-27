import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.special as sp

theta=np.linspace(0,np.pi,100) #polar angle
phi=np.linspace(0,2*np.pi,100) #azimuthal angle
theta,phi=np.meshgrid(theta,phi)
l=2 #ang momentum quantum no
m=-2 #mag orbital quantum no

Y=sp.sph_harm(m,l,phi,theta) #spherical harmonics

if m<0:
  Y=np.sqrt(2)*(-1)**m*Y.imag
elif m>0:
  Y=np.sqrt(2)*(-1)**m*Y.real

x=abs(Y)*np.sin(theta)*np.cos(phi)
y=abs(Y)*np.sin(theta)*np.sin(phi)
z=abs(Y)*np.cos(theta)

fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.plot_surface(x,y,z,cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Spherical Harmonics (l=2, m=-2)')
plt.show()
