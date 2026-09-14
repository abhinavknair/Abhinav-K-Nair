import numpy as np

U1=np.random.uniform(0,1,1)
U2=np.random.uniform(0,1,1)

R=np.sqrt(-2*np.log(U1))
theta=2*np.pi*U2

Z1=R*np.cos(theta)
Z2=R*np.sin(theta)
print('U1=',U1)
print('U2=',U2)
print('Z1=',Z1)
print('Z2=',Z2)

#U1,U2 - uniformly distributed random numbers
#Z1,Z2 - normally distributed random numbers
