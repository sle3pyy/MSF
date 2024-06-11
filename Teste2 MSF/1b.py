import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0 # condição inicial, tempo [s]
tf = 1 # limite do domínio, tempo final [s]
dt = 0.001 # passo [s]
v0 = 100/3.6 # velocidade inicial [m/s]
ang = 16 # ângulo de lançamento [graus]
r0 = np.array([-20, 0, 0]) # condição inicial, posição inicial [m]
v0 = np.array([v0*np.cos(ang*np.pi/180), v0*np.sin(ang*np.pi/180),0]) # condição inicial, velocidade inicial [m/s]
w = np.array([0,0,-10]) # condição inicial, velocidade angular CONSTANTE [rad/s]
g = 9.8 # aceleração gravítica [m/s^2]
D = 0.0127 # coeficiente de resistência do ar [m^-1]
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
    Fmagnus = A * rho * R * np.cross(w,v[:,i]) / (2 * m)
    a[:, i] = -D * np.linalg.norm(v[:,i]) * v[:,i] + Fmagnus
    a[1, i] -= g
    v[:, i + 1] = v[:, i] + a[:, i] * dt
    r[:, i + 1] = r[:, i] + v[:, i] * dt

plt.plot(r[0,:], r[1,:], 'b-')
plt.xlabel("Posição horizontal, r_x [m]")
plt.ylabel("Posição vertical, r_y [m]")
plt.show()


# indice e tempo para o qual a bola atinge a "linha de fundo", ie, instante de
izzero = np.argmin(np.abs(r[0,:]))

print(" A bola passa a linha de baliza á altura de", r[1,izzero], "m")
print(" E a z= ", r[2,izzero], "m")
print(" Logo é golo")

#aluno 119042