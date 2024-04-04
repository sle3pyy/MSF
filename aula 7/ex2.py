import numpy as np
import matplotlib.pyplot as plt

t0=0
tf=10
dt=0.001
v0=1.5*np.pi
x0=1

G=4 *np.pi**2
m=3.003e-6

t=np.arange(t0,tf,dt)  

a=np.zeros([np.size(t),2])
v=np.zeros([np.size(t),2])
x=np.zeros([np.size(t),2])

v[0,:]=np.array([0,v0])
x[0,:]=np.array([x0,0])

for i in range(np.size(t)-1):
    a[i,:]= -G*x[i,:]/np.linalg.norm(x[i,:])**3
    v[i+1,:]=v[i,:]+a[i,:]*dt
    x[i+1,:]=x[i,:]+v[i+1,:]*dt


plt.plot(x[:,0],x[:,1],"r-")
plt.show()
