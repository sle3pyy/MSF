import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0 # condição inicial, tempo [s]
tf = 2 # limite do domínio, tempo final [s]
dt = 0.01 # passo [s]
v0 = 130/3.6 # velocidade inicial [m/s]
ang = 10 # ângulo de lançamento [graus]
r0 = np.array([-10, 1, 0]) # condição inicial, velocidade inicial [m/s]
v0 = np.array([v0*np.cos(ang*np.pi/180), v0*np.sin(ang*np.pi/180),0]) # condição inicial, velocidade inicial [m/s]
w = np.array([0,0,-100]) # condição inicial, velocidade angular CONSTANTE [rad/s]
g = 9.8 # aceleração gravítica [m/s^2]
v_T = 100.0 * 1000 / 3600 # velocidade terminal [m/s]
D = g / v_T ** 2 # coeficiente de resistência do ar [m^-1]
R = 0.067/2 # raio da bola [m]
A = np.pi * R ** 2 # área da secção da bola
m = 0.057 # massa da bola [kg]
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
    a[:, i] = -D * np.linalg.norm(v[:,i]) * v[:,i] + A * rho * R * np.cross(w,v[:,i]) / (2 * m)
    a[1, i] -= g
    v[:, i + 1] = v[:, i] + a[:, i] * dt
    r[:, i + 1] = r[:, i] + v[:, i] * dt

plt.plot(r[0,:], r[1,:], 'b-')
plt.xlabel("Posição horizontal, r_x [m]")
plt.ylabel("Posição vertical, r_y [m]")
plt.show()

# indice e tempo para o qual a bola atinge a "linha de fundo", ie, instante de
# tempo a partir do qual a coordenada x da bola se torna negativa.
izzero = np.argmin(np.abs(r[1,:]))
txzero = t[izzero]

hmax = np.argmax(r[1,:])

print("Altura máxima atingida pela bola:", r[1,hmax], "m")
print("Tempo correspondente à altura máxima, tmax =", t[hmax], "s")
      
print("Tempo correspondente a y=0, txzero =", txzero, "s")
print("Coordenadas de y~0:")
print(" x = ", r[0,izzero], "m")
print(" y = ", r[1,izzero], "m")
print(" z = ", r[2,izzero], "m")