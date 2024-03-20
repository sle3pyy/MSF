import numpy as np
import matplotlib.pyplot as plt
import sympy

h = 1000
vt1 = 60
vt2 = 5
g = 9.8
D1 = g/vt1**2
D2 = g/vt2**2
t0 = 0
tf = 100
dt = 0.01
rho1 = 1.225  # density of air at sea level in kg/m^3

t = np.arange(t0,tf, dt)
v1 = np.empty(np.size(t))
y1 = np.empty(np.size(t))
a1 = np.empty(np.size(t))
v2 = np.empty(np.size(t))
y2 = np.empty(np.size(t))
a2 = np.empty(np.size(t))
vA = np.empty(np.size(t))
yA = np.empty(np.size(t))
aA = np.empty(np.size(t))
y1[0] = h
y2[0] = h
yA[0] = h

for i in range(np.size(t)-1):
    a1[i] = -g - D1*v1[i]*np.abs(v1[i])
    v1[i+1]=v1[i]+a1[i]*dt  
    y1[i+1]= y1[i]+v1[i]*dt

    a2[i] = -g - D2*v2[i]*np.abs(v2[i])
    v2[i+1]=v2[i]+a2[i]*dt
    y2[i+1]= y2[i]+v2[i]*dt

    rho = (rho1*np.exp(-0.1378*(yA[i])/1000)) # calculate the density at the current height
    if t[i] < 20:
        aA[i] = -g - D1*rho*vA[i]*np.abs(vA[i])
    else:
        aA[i] = -g - D2*rho*vA[i]*np.abs(vA[i])

    vA[i+1] = vA[i] + aA[i]*dt
    yA[i+1] = yA[i] + vA[i]*dt
    

        
    

index = np.argmin(np.abs(y1))   # Find the index of the value in y1 that is closest to 0
time_when_y1_is_zero = t[index] # Use this index to get the corresponding time from t
speed_when_y1_is_zero = v1[index]
print("The moment when y1 is 0 is at t =", time_when_y1_is_zero, "and the speed is", speed_when_y1_is_zero*3.6, "km/h")

index = np.argmin(np.abs(y2))   # Find the index of the value in y1 that is closest to 0
time_when_y2_is_zero = t[index] # Use this index to get the corresponding time from t
speed_when_y2_is_zero = v2[index]
print("The moment when y2 is 0 is at t =", time_when_y2_is_zero, "and the speed is", speed_when_y2_is_zero*3.6, "km/h")

index = np.argmin(np.abs(yA))   # Find the index of the value in y1 that is closest to 0
time_when_yA_is_zero = t[index] # Use this index to get the corresponding time from t
speed_when_yA_is_zero = vA[index]
print("The moment when yA is 0 is at t =", time_when_yA_is_zero, "and the speed is", speed_when_yA_is_zero*3.6, "km/h")

plt.plot(t,yA,"r-")

plt.show()    


