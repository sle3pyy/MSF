import numpy as np
import matplotlib.pyplot as plt
import sympy

t0=0  # initial time
tf=4 # final time
dt=0.01  # time step
vt = 6.8
g = 9.8
D=(g/vt**2)
t = np.arange(t0,tf, dt) 
a = np.empty(np.size(t))
v= np.empty(np.size(t))
y= np.empty(np.size(t))

for i in range(np.size(t)-1):
    a[i] = g - D*v[i]*np.abs(v[i])
    v[i+1]=v[i]+a[i]*dt  
    y[i+1]=y[i]+v[i]*dt  


# Find the index of the value in t that is closest to 1
index = np.argmin(np.abs(t - 1))

# Use this index to get the corresponding speed from v
speed_at_t1 = v[index]

print("The speed at t=1 is", speed_at_t1)

plt.plot(t,a,"r-")
plt.plot(t,v,"b-")
plt.show()