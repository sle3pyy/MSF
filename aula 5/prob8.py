import numpy as np
import matplotlib.pyplot as plt

r=0.11          #raio da bola
A=np.pi*r**2    #área de secção de corte da bola m^2
rho=1.225       #massa volumica do ar kg/m^3

omega= np.array([0,0,10]) #vetor de velocidade angular rad/s
v= np.array([0,1,0])     #vetor de velocidade linear m/s

F= 0.5*rho*A*np.cross(omega,v) #força de arrasto
print("a força de arrasto é:", F)
