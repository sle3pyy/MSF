import numpy as np 
import matplotlib.pyplot as plt
import sympy 

t0=0
tf=4
x0=0
v0=0
dt=0.01
g=9.8

t= np.arange(t0,tf,dt)   #dominio
x_exata=np.empty(np.size(t))  #solução exata
v= np.empty(np.size(t))  #array de velocidade
x= np.empty(np.size(t))  #array de posição

v[0]=v0
for i in range(np.size(t)-1):
    v[i+1] = v[i]+g*dt   #uso do metodo de Euler para a velocidade
    x[i+1] = x[i]+v[i]*dt  #uso do metodo de Euler para a posição
    x_exata[i]=0.5*g*t[i]**2  #solução exata

i3=int((3-t0)/dt)        #método de Euler para t=3
i2=int((2-t0)/dt)        #método de Euler para t=2
print('x(2)=',x[i2])
print('v(3)=',v[i3])
print("desvio=", np.abs(x[i2]-x_exata[i2]))  #desvio entre a solução exata e a solução numérica