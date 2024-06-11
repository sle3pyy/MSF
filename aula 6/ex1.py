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

imax = np.argmax(r[1,:])
tmax = t[imax]
print("Tempo correspondente à altura máxima, tmax = ", tmax, "s")
print("Altura máxima, ymax = ", r[1,imax], "m")
 

izero = np.size(r[1,:]) - np.size(r[1, r[1,:]<0]) # aqui usamos a "indexação condici
tzero = t[izero]
print("Tempo correspondente ao alcance máximo, tzero = ", tzero, "s")
print("Alcance máximo da bola, xmax = ", r[0,izero], "m")

plt.plot(r[0,:],r[1,:],"r-")
plt.show()
