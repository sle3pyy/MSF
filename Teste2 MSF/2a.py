import numpy as np
import matplotlib.pyplot as plt

m=0,5
t0=0
tf=2
dt=0.01
K=2

t=np.arange(t0,tf,dt)

Ep = np.zeros([np.size(t),1])

for i in range(np.size(t)-1):
    Ep[i] = K*((t[i]-0.5)**2)*((t[i]+0.5)**2)

plt.plot(t,Ep,"r-")
plt.show()    

#aluno 119042