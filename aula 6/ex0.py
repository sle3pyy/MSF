import numpy as np
import matplotlib.pyplot as plt


t0 = 0.0 # condição inicial, tempo [s]
tf = 2.0 # limite do domínio, tempo final [s]
dt = 0.01 # passo [s]
v0 = 100.0 * 1000 / 3600 # condição inicial, módulo da velocidade inicial [m/s]
theta0 = 10 * np.pi / 180.0 # condição inicial, ângulo do vetor velocidade inicial [ra
g = 9.8 # aceleração gravítica [m/s^2]

# inicializar domínio [s]
t = np.arange(t0, tf, dt)

# inicializar solução, aceleração [m/s^2]
a = np.zeros([2, np.size(t)])
a[1,:] = -g # aceleração é um vetor constate (ao longo do -y)

# inicializar solução, velocidade [m/s]
v = np.zeros([2, np.size(t)])
v[:,0] = v0 * np.array([np.cos(theta0), np.sin(theta0)]) # velocidade para t = 0

# inicializar solução, posição [m]

r = np.zeros([2, np.size(t)])
r[:,0] = np.array([0.0, 0.0]) # posição para t = 0


for i in range(np.size(t) - 1):
    v[:, i + 1] = v[:, i] + a[:, i] * dt
    r[:, i + 1] = r[:, i] + v[:, i] * dt


 
plt.plot(r[0,:], r[1,:], 'b-')
plt.xlabel("Posição horizontal, r_x [m]")
plt.ylabel("Posição vertical, r_y [m]")
plt.show()

tm = v[1,0] / g # tempo para atingir altura máxima
ym = 0.0 + (v[1,0]) ** 2 / (2 * g) # altura máxima
tsolo = 2 * v[1,0] / g # tempo para atingir alcance máximo
xsolo = 2 * v[0,0] * v[1,0] / g # alcance máximo

print("tm =", tm, "s")
print("ym =", ym, "m")
print("tsolo =", tsolo, "s")
print("xsolo =", xsolo, "m")