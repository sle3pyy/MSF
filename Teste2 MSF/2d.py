import numpy as np
import matplotlib.pyplot as plt

m=0.5 #massa do corpo
x0=0    #posição inicial
xf=2   #posição final
dt=0.01 #passo
v0 = 0 #velocidade inicial
K=2 #constante (J/m^4)

x=np.arange(x0,xf,dt)

Ep = np.zeros([np.size(x),1])
Fx = np.zeros([np.size(x),1])
Ax = np.zeros([np.size(x),1])
Vx = np.zeros([np.size(x),1])

for i in range(np.size(x)-1):
    Fx[i] = -4*K*(x[i]**3)+K*x[i] #força exercida no corpo -> -4Kx^3+Kx

    Ep[i] = -K*x[i]**4 + 0.5*K*x[i]**2 #energia potencial (F=-dEp/dx) -> -Kx^4+0.5Kx^2

    Ax[i] = Fx[i] / m  #aceleração do corpo (F=ma) -> -4Kx^3+Kx = ma -> a = -8kx^3+2kx

    Vx[i] =  -2*K*x[i]**4+K*x[i]**2+v0 #velocidade do corpo (integral da aceleração) -> -2Kx^4+Kx+v0

# Energia cinética
Ec = 0.5 * m * Vx ** 2
# Energia total
Et = Ep + Ec

#encontrar a velocidade em x=0.5
indices = np.where(np.isclose(x, 0.5, atol=1e-6))

index_x_05 = indices[0][0]
speed_x_05 = Vx[index_x_05]
print("The speed at x=0.5 is:", speed_x_05[0],"m/s")

#aluno 119042