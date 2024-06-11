import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0 # condição inicial, tempo [s]
tf = 1.0 # limite do domínio, tempo final [s]
dt = 0.01 # passo [s]
r0 = np.array([1, 0.0, 0]) # condição inicial, velocidade inicial [m/s]
v0 = np.array([25.0, 5.0,0]) # condição inicial, velocidade inicial [m/s]
w = 390.0 # condição inicial, velocidade angular CONSTANTE [ra
g = 9.8 # aceleração gravítica [m/s^2]
v_T = 100.0 * 1000 / 3600 # velocidade terminal [m/s]
D = g / v_T ** 2 # coeficiente de resistência do ar [m^-1]
R = 0.11 # raio da bola [m]
A = np.pi * R ** 2 # área da secção da bola
m = 0.45 # massa da bola [kg]
rho = 1.225 # densidade do ar [kg/m^3]

# inicializar domínio [s]
t = np.arange(t0, tf, dt)

# inicializar solução, aceleração [m/s^2]
a = np.zeros([3, np.size(t)])

# inicializar solução, velocidade [m/s]
v = np.zeros([3, np.size(t)])
v[:,0] = v0

# inicializar solução, posição [m]
r = np.zeros([3, np.size(t)])
r[:,0] = r0

for i in range(np.size(t) - 1):
    a[0, i] = -D * np.linalg.norm(v[:,i]) * v[0,i] + A * rho * R * w * v[2,i] / (2 * m)
    a[1, i] = -g - D * np.linalg.norm(v[:,i]) * v[1, i]
    a[2, i] = -D * np.linalg.norm(v[:,i]) * v[2,i] - A * rho * R * w * v[0,i] / (2 * m)
    v[:, i + 1] = v[:, i] + a[:, i] * dt
    r[:, i + 1] = r[:, i] + v[:, i] * dt

plt.plot(r[0,:], r[1,:], 'b-')
plt.xlabel("Posição horizontal, r_x [m]")
plt.ylabel("Posição vertical, r_y [m]")
plt.show()

print(r[2,:])

# indice e tempo para o qual a bola atinge a "linha de fundo", ie, instante de
# tempo a partir do qual a coordenada x da bola se torna negativa.
ixzero = np.argmin(np.abs(r[0,:]))
#print("Tempo correspondente ao cruzamento da linha de fundo, txzero =", txzero, "s")
print("Coordenadas da bola quando cruza a linha de fundo:")
print(" x = ", r[0,ixzero], "m")
print(" y = ", r[1,ixzero], "m")
print(" z = ", r[2,ixzero], "m")

