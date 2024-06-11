import numpy as np
import matplotlib.pyplot as plt

y0= 0
x0= 0
t0 = 0
tf = 1
dt= 0.01
v0 = 100/3.6
ang = 10
v0x = v0*np.cos(ang*np.pi/180)
v0y = v0*np.sin(ang*np.pi/180)
Vabs = np.sqrt(v0x**2+v0y**2)
g=9.8
D=g/v0**2
t=np.arange(t0,tf,dt)  

v=np.zeros([np.size(t),2])
r=np.zeros([np.size(t),2])
a=np.zeros([np.size(t),2])

a[0,:]=np.array([0,-9.8])
v[0,:]=np.array([v0x,v0y])
r[0,:]=np.array([x0,0])


for i in range(np.size(t)-1):
    a[i,1]= -9.8 - D*np.linalg.norm(v[i,:])*v[i,1]
    a[i,0]= - D*np.linalg.norm(v[i,:])*v[i,0]
    
    v[i+1,1]=v[i,1]+a[i,1]*dt
    r[i+1,1]=r[i,1]+v[i,1]*dt

    v[i+1,0]=v[i,0]+a[i,0]*dt
    r[i+1,0]=r[i,0]+v[i,0]*dt

max_arg = np.argmax(r[:,1])
print("The maximum height is:",r[max_arg,1])

zero_indices = []

for i in range(len(r[:,1])):
    # If y is approximately 0, store the index
    if np.isclose(r[i,1], 0, atol=0.04):
        zero_indices.append(i)
    # If we've found the second y=0, break the loop
    if len(zero_indices) == 2:
        break

distance_x = r[zero_indices[1], 0] - r[zero_indices[0], 0]
print("The distance traveled in the x-direction between the first and second y=0 is:", distance_x)

plt.plot(r[:,0],r[:,1],"r-")
plt.show()
