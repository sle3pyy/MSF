import numpy as np 
import matplotlib.pyplot as plt
import sympy 
# Constants
t0=0  # initial time
tf=4 # final time
y0 = 0  # initial position
v0 = 10  # initial velocity
vt = 100*1000/3600  # terminal velocity
dt=0.0001  # time step

g = 9.8  # acceleration due to gravity
D = g/vt**2  # air resistance coefficient

# Time
t = np.arange(t0,tf, dt)  # time interval from 0 to 10 seconds with 100 points
y= np.empty(np.size(t))  # position array
v= np.empty(np.size(t))  # velocity array
a = np.empty(np.size(t))  # acceleration array

v[0]=v0
y[0]=y0

for i in range(np.size(t)-1):
    a[i] = -g - D*v[i]*np.abs(v[i])  # acceleration
    v[i+1]=v[i]+a[i]*dt  # velocity
    y[i+1]=y[i]+v[i]*dt  # position

imax = np.argmax(y) # index of maximum value of y
tmax = t[imax] # time of maximum value of y

izero = np.size(y)-np.size(y[y<0]) # index of the 2nd zero of y
tzero = t[izero] # time of the 2nd zero of y

print("t0=",tzero)
print("ymax=",y[imax])    
print("tmax=",tmax)
plt.plot(t,y,"r-")
plt.show()
