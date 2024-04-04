import numpy as np
import matplotlib.pyplot as plt

t0=0
tf=2
x0=0
y0=0
v0=100*1000/3600
theta0=10*np.pi/180
dt=0.01
g=9.8
vt=v0
D=g/vt**2

t=np.arange(t0,tf,dt)

a=np.zeros([2,np.size(t)])

v=np.zeros([2,np.size(t)])
v[:,0]=v0*np.array([np.cos(theta0),np.sin(theta0)])

r=np.zeros([2,np.size(t)])
r[:,0]=np.array([x0,y0])

for i in range(np.size(t)-1):
    a[0,i]= -D*np.linalg.norm(v)*v[0,i]
    a[1,i]= -g - D*np.linalg.norm(v)*v[1,i]
    v[:,i+1]=v[:,i]+a[:,i]*dt
    r[:,i+1]=r[:,i]+v[:,i]*dt

hmax=np.argmax(r[1,:])
print("Tempo de altura maxima:",hmax," de altura:",r[1,hmax])    

plt.plot(r[0,:],r[1,:],"r-")
plt.show()
