import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0        # condição inicial, tempo [s]
tf = 100.0      # limite do domínio, tempo final [s]
dt = 0.01       # passo [s]
r0 = 0.0        # condição inicial, posição inicial [m]
v0 = 1.0        # condição inicial, velocidade inicial [m/s]
g = 9.8         # aceleração gravítica [m/s^2]
P = 350.0       # Potência de propulsão [W]
mu = 0.004      # coeficiente de resistência do piso []
C_res = 0.9     # coeficiente de resistência do ar [s]
rho_ar = 1.225  # densidade do ar [kg/m3]
A = 0.35        # área frontal efetiva da ciclista [m2]
m = 70.0        # massa da ciclista (+ bicicleta) [kg]

# inicializar domínio temporal [s]
t = np.arange(t0, tf, dt)

# inicializar solução
a = np.zeros(np.size(t)) # aceleração [m/s2]
v = np.zeros(np.size(t)) # velocidade [m/s]
r = np.zeros(np.size(t)) # posição [m]
r[0] = r0
v[0] = v0

# método de Euler
for i in range(np.size(t) - 1):
    a[i] = P / (m * v[i]) - C_res * A * rho_ar * v[i] ** 2 / (2 * m) - mu * g
    v[i + 1] = v[i] + a[i] * dt
    r[i + 1] = r[i] + v[i] * dt

v_T = v[-1]
print("a) Velocidade terminal, v_T = {0:.4f} m/s \n".format(v_T))

i_rs = np.size(r[r>=500], 0) - 1
rs = r[i_rs]
ts = t[i_rs]
print("b) Tempo decorrido para r = 500 m, t = {0:.2f} s \n".format(ts))


i_r200 = np.argmax(r >= 200)
r200 = r[i_r200]
t200 = t[i_r200]
print("c) Velocidade em r = 200 m, v(200 m) = {0:.4f} m/s".format(v[i_r200]))
print("v(200m) é {0:.2f}% da velocidade terminal".format(v[i_r200] / v_T * 100))


plt.plot(t, r, 'b-')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Velocidade, v [m/s]")
plt.show()
