import numpy as np
import matplotlib.pyplot as plt

y0 = 3
x0 = 0
t0 = 0
tf = 3
dt= 0.001
v0 = 200/3.6
ang = 10
v0x = v0*np.cos(ang*np.pi/180)
v0y = v0*np.sin(ang*np.pi/180)
Vabs = np.sqrt(v0x**2+v0y**2)
g=9.8
D=g/6.8**2

t=np.arange(t0,tf,dt)

v=np.zeros([np.size(t),2])
r=np.zeros([np.size(t),2])
a=np.zeros([np.size(t),2])

a[0,:]=np.array([0,-g])
v[0,:]=np.array([v0x,v0y])
r[0,:]=np.array([x0,y0])

for i in range(np.size(t)-1):
    a[i,1]= -9.8 - D*np.linalg.norm(v[i,:])*v[i,1]   
    a[i,0]= - D*np.linalg.norm(v[i,:])*v[i,0]

    v[i+1,1]=v[i,1]+a[i,1]*dt
    r[i+1,1]=r[i,1]+v[i,1]*dt    
    v[i+1,0]=v[i,0]+a[i,0]*dt
    r[i+1,0]=r[i,0]+v[i,0]*dt   

plt.plot(r[:,0],r[:,1],"r-")
plt.show()

first_x = r[0,0]

for i in range(1, len(r[:,1])):
    if r[i-1,1] > 0 and r[i,1] <= 0:
        x_at_y_zero = r[i,0]
        break

distance_x = x_at_y_zero - first_x
print("The distance traveled in the x-direction from the first point to the point where y=0 is:", distance_x)

plt.plot(r[:,0],r[:,1],"r-")
plt.show()
    



