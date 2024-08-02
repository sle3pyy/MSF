import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0        # condição inicial, tempo [s]
tf = 200.0      # limite do domínio, tempo final [s]
dt = 0.001      # passo [s]
x0 = 0.2        # condição inicial, posição inicial [m]
v0 = 0.0        # condição inicial, velocidade inicial [m/s]
m = 2.0         # massa [kg]
k = 0.5         # constante da mola [N/m]
b = 0.2         # constante de amortecimento [kg/s]

# inicializar domínio temporal [s]
t = np.arange(t0, tf, dt)

# inicializar solução
a = np.zeros(np.size(t)) # aceleração [m/s2]
v = np.zeros(np.size(t)) # velocidade [m/s]
x = np.zeros(np.size(t)) # posição [m]
x[0] = x0
v[0] = v0

# método de Euler-Cromer
for i in range(np.size(t) - 1):
    a[i] = - (k * x[i] - b * v[i]) / m
    v[i + 1] = v[i] + a[i] * dt
    x[i + 1] = x[i] + v[i+1] * dt

plt.plot(t, x, 'b-')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Posição, x [m]")
plt.show()

plt.plot(t, v, 'r-')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Velocidade, v [m/s]")
plt.show()
