import numpy as np
import matplotlib.pyplot as plt

t0=0    
tf=1
dt=0.01

vt=100
D=g/vt**2
g=9.8
rho=1.225
R=0.11
A=np.pi*R**2
m=0.45


r0=np.array([0,0,23.8])
v0=np.array([25,5,-50])
w=np.array([0,390,0])


t=np.arange(t0,tf,dt)

a=np.zeros([3,np.size(t)])

v=np.zeros([3,np.size(t)])
v[:,0]=v0

r=np.zeros([3,np.size(t)])
r[:,0]=r0

for i in range(np.size(t)-1):
    a[0,i]= -D*np.linalg.norm(v)*v[0,i]+A*rho*R*w*v[2,i]/(2*m)
    a[1,i]= -g - D*np.linalg.norm(v)*v[1,i]
    a[2,i]= -D*np.linalg.norm(v)*v[2,i]-A*rho*R*w*v[0,i]/(2*m)
    v[:,i+1]=v[:,i]+a[:,i]*dt
    r[:,i+1]=r[:,i]+v[:,i]*dt

plt.plot(r[0,:],r[1,:],"r-")
plt.show()    