import numpy as np
import matplotlib.pyplot as plt

# Condições iniciais
t0 = 0.0 # condição inicial, tempo [s]
tf = 3.0 # limite do domínio, tempo final [s]
dt = 0.001 # passo [s]
v0 = 0.0 # condição inicial, módulo da velocidade inicial [m/s]
x0 = 0.0 # condição inicial, coordenada x da posição inicial [m]
y0 = 11.0 # condição inicial, coordenada y da posição inicial [m]
M = 0.2 # Massa do corpo [kg]
g = 9.80665 # aceleração gravitacional (valor standard) [m/s^2]


# Derivada de y em ordem a x
# y(x) = 11 - x para x < 10 de outra forma y(x) = 0
# dy/dx = -1 de outra forma dy/dx = 0
def dydx_func(x: float) -> float:
    return -1 if x < 10.0 else 0.0

# inicializar domínio [ano]
t = np.arange(t0, tf, dt)

# inicializar solução, aceleração a 1D [m/s^2]
a = np.zeros(np.size(t))

# inicializar solução, velocidade [m/s]
v = np.zeros(np.size(t))
v[0] = v0

# inicializar solução, posição [m]
s = np.zeros(np.size(t))
s[0] = x0
x = np.zeros(np.size(t))
y = np.zeros(np.size(t))
x[0] = x0
y[0] = y0
theta = np.zeros(np.size(t))

for i in range(np.size(t) - 1):
    # ângulo θ
    theta[i] = -np.arctan(dydx_func(x[i]))

    # aceleração
    a[i] = g * np.sin(theta[i])

    # Método de Euler-Cromer
    v[i + 1] = v[i] + a[i] * dt
    s[i + 1] = s[i] + v[i + 1] * dt

    # posição carteziana
    x[i + 1] = x[i] + (s[i + 1] - s[i]) * np.cos(theta[i])
    y[i + 1] = y[i] - (s[i + 1] - s[i]) * np.sin(theta[i])


#plot posiçao x tempo
#plt.plot(t, s, 'b-')
plt.xlabel("t [s]")
plt.ylabel("s [m]")

print("Espaço percorrido, s(t = 3 s) = {0:.2f} m".format(s[-1]))
print("Alcançe, x(t = 3 s) = {0:.2f} m".format(x[-1]))

v1 = v
print("A velocidade final v = {0:.2f} m/s²".format(v1[-1]))

x1 = x # guardar para mais tarde
y1 = y
# Energia potencial
E_p1 = M * g * y1
# Energia cinética
E_c1 = 0.5 * M * v1 ** 2
# Energia total
E_t1 = E_p1 + E_c1

#plt energia potencial, cinética e mecanica
plt.plot(t, E_p1, 'r-', t, E_c1, 'g-', t, E_t1, 'b-')
plt.xlabel("t [s]")
plt.ylabel("Energia [J]")
plt.show()
