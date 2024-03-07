import numpy as np 
import matplotlib.pyplot as plt
import sympy 

t0=0
v0=0
dt=0.001
tf=10

a=5

t=np.arangre(t0,tf,dt)
v=np.empty(np.size(t))

v[0]=0
for i in range(np.size(t)):
    t[i+1]=t[i]+dt

